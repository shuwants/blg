from flask import request, redirect, url_for, render_template, flash, session # 後使用も含め必要パッケージインストール
from flask_blog import app # __init__.pyで作成したappをインポート


@app.route('/')
def show_entries():
	return render_template('entries/index.html')
# template以下に有るentries/index.htmlを返して(レンダリングして)あげると言う設定
# パスにtemplateを設定しないのは、flaskではtemplatesフォルダ以下に自動でhtmlファイルがある(ルール)と認識するから。
