from flask import request, redirect, url_for, render_template, flash, session  # 後使用も含め必要パッケージインストール
from flask_blog import app  # __init__.pyで作成したappをインポート
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required
from flask import Blueprint

entry = Blueprint('entry', __name__)


@entry.route('/')
@login_required
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)

# template以下に有るentries/index.htmlを返して(レンダリングして)あげると言う設定
# パスにtemplateを設定しないのは、flaskではtemplatesフォルダ以下に自動でhtmlファイルがある(ルール)と認識するから。

# 元 flask_bog/viewsからshow_entries部分のみコピー
# 分けた事で、今後記事の作成・一覧など記事に関連するビューは、entries.pyのみアップデートすればよくなった
# また、モデルごとにビューを用意することでモデルとビューが１対１の紐付けになり、わかりやすくなった。


# add_entryビューを作成、投稿内容を受信してデータベースに保存、そしてadd_entryビューを追加
@entry.route('/entries', methods=['POST'])  # ログインフォーム作成時と同様、データ送信にはPOSTメソッド指定。
@login_required
def add_entry():
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )  # 送られてきた記事タイトル都内容についてのモデルインスタンスを作成。
    db.session.add(entry)  # 作成されたモデルインスタンスに対して、これらの処理を行う事で新しい記事内容をデータベースに保存。
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('entry.show_entries'))


@entry.route('/entries/new', methods=['GET'])  # new_entryビューを追加 p856
@login_required
def new_entry():
    return render_template('entries/new.html')


@entry.route('/entries/<int:id>', methods=['GET'])  # <id>だけもok、必ず整数を受け取る様制限したいので<int:id>と書くことでidに整数以外の値が渡された時にエラーになる様に。
@login_required
def show_entry(id):  # show_entry(id)と引き数名を追加し、変数idを参照出来る様にする
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)
# show_entryメソッド内では、entry = Entry.query.get(id)と書くだけで渡されたidの記事をdbから取得する事が出来る。


@entry.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)


@entry.route('/entries/<int:id>/update', methods=['POST'])
@login_required
def update_entry(id):
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)  # 作成時はaddだったが、更新はこれ。
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('entry.show_entries'))


@entry.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('entry.show_entries'))
