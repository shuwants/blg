from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy ライブラリをインストール

app = Flask(__name__) # アプリケーション本体
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app) # これで他のプログラムはdbと言う変数を参照する事でデータベースを扱える様になった。

from flask_blog.views.entries import entry  # __init__.pyにBlueprintアプリケーションを登録
app.register_blueprint(entry, url_prefix='/users')

from flask_blog.views import views, entries
