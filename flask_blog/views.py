from flask import request, redirect, url_for, render_template, flash, session # 後使用も含め必要パッケージインストール
from flask_blog import app # __init__.pyで作成したappをインポート


@app.route('/')
def show_entries():
	if not session.get('logged_in'):
		return redirect('/login')
	return render_template('entries/index.html')
# template以下に有るentries/index.htmlを返して(レンダリングして)あげると言う設定
# パスにtemplateを設定しないのは、flaskではtemplatesフォルダ以下に自動でhtmlファイルがある(ルール)と認識するから。

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			print('ユーザ名が異なります')
		elif request.form['password'] != app.config['PASSWORD']:
			print('パスワードが異なります')
		else:
			session['logged_in'] = True
			return redirect('/') # 直接リンク名では無く、ビューに定義しているメソッド名を指定↓したコードが下記。
	return render_template('login.html')

# 正しい場合には/にリダイレクト、そうで無い場合はrender_template('login.html')のログインフォームを再度表示。

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect('/') # 直接リンク名では無く、ビューに定義しているメソッド名を指定↓したコードが下記。
