from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy ライブラリをインストール

app = Flask(__name__) # アプリケーション本体
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app) # これで他のプログラムはdbと言う変数を参照する事でデータベースを扱える様になった。

import flask_blog.views
