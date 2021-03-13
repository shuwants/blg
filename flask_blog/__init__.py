from flask import Flask

app = Flask(__name__) # アプリケーション本体
app.config.from_object('flask_blog.config')

import flask_blog.views
