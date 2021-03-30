from flask_blog import db
from datetime import datetime

class Entry(db.Model): # 実際のモデルの定義。モデル(今回モデル名はEntry)はclassとして定義。
    __tablename__ = 'entries' # 実際のデータベースに格納されるテーブル名。実際はEntryモデルを経由して操作。
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None): # モデルが作成された時の標準の動作。
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self): # 無くても良いがあると嬉しい、実際に記事モデルが参照された時のコンソールでの出力形式について
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)

