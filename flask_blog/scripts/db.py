from flask_script import Command
from flask_blog import db

# モデルで定義した内容をデータベースに反映させる、の内コーソール実行では無くスクリプトというファイルでの実行。

class InitDB(Command): # InitDBはクラス名。好きな名前を付けて良い。
    "create database" # クラスの説明。後で見て分かり易い内容が吉。

    def run(self): # 実際にスクリプトで実行される内容。
        db.create_all() # →これでモデル定義が反映される。