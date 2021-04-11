from flask import request, redirect, url_for, render_template, flash, session  # 後使用も含め必要パッケージインストール
from flask_blog import app  # __init__.pyで作成したappをインポート
from flask_blog import db
from flask_blog.models.entries import Entry


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)

# template以下に有るentries/index.htmlを返して(レンダリングして)あげると言う設定
# パスにtemplateを設定しないのは、flaskではtemplatesフォルダ以下に自動でhtmlファイルがある(ルール)と認識するから。

# 元 flask_bog/viewsからshow_entries部分のみコピー
# 分けた事で、今後記事の作成・一覧など記事に関連するビューは、entries.pyのみアップデートすればよくなった
# また、モデルごとにビューを用意することでモデルとビューが１対１の紐付けになり、わかりやすくなった。


# add_entryビューを作成、投稿内容を受信してデータベースに保存、そしてadd_entryビューを追加
@app.route('/entries', methods=['POST'])  # ログインフォーム作成時と同様、データ送信にはPOSTメソッド指定。
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )  # 送られてきた記事タイトル都内容についてのモデルインスタンスを作成。
    db.session.add(entry)  # 作成されたモデルインスタンスに対して、これらの処理を行う事で新しい記事内容をデータベースに保存。
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))


@app.route('/entries/new', methods=['GET'])  # new_entryビューを追加 p856
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')
