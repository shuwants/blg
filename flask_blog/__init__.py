from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy ライブラリをインストール

db = SQLAlchemy() # これで他のプログラムはdbと言う変数を参照する事でデータベースを扱える様になった。


def create_app():
    app = Flask(__name__) # アプリケーション本体
    app.config.from_object('flask_blog.config')

    db.init_app(app)

    from flask_blog.views.views import view
    app.register_blueprint(view)

    from flask_blog.views.entries import entry  # __init__.pyにBlueprintアプリケーションを登録
    app.register_blueprint(entry, url_prefix='/users')

    return app

# from flask_blog.views import views, entries => グローバルスコープで作成していた際の最後の1行
