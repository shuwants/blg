from flask import request, redirect, url_for, render_template, flash, session # 後使用も含め必要パッケージインストール
from flask_blog import app # __init__.pyで作成したappをインポート
from functools import wraps


def login_required(view):
	@wraps(view)
	def inner(*args, **kwargs):
		if not session.get('logged_in'):
			return redirect(url_for('entry.login'))
		return view(*args, **kwargs)
	return inner

# 当初ここに書いたshow_entriesをflask_blog/views/entries.pyに移動


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			flash('ユーザ名が異なります')
		elif request.form['password'] != app.config['PASSWORD']:
			flash('パスワードが異なります')
		else:
			session['logged_in'] = True
			flash('ログインしました')
			return redirect(url_for('entry.show_entries')) # 直接リンク名では無く、ビューに定義しているメソッド名を指定↓したコードが下記。
	return render_template('login.html')
# 正しい場合には/にリダイレクト、そうで無い場合はrender_template('login.html')のログインフォームを再度表示。


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('ログアウトしました')
	return redirect(url_for('entry.show_entries')) # 直接リンク名では無く、ビューに定義しているメソッド名を指定↓したコードが下記。


@app.errorhandler(404)  # 存在しないURLにアクセスした時など、404エラーが発生した時に行わせる処理を定義する
def non_existant_route(error):
	return redirect(url_for('login'))  # これでログインURLにリダイレクトさせる
