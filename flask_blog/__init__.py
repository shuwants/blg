from flask import Flask

app = Flask(__name__) # アプリケーション本体

import flask_blog.views
