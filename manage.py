from flask_script import Manager
from flask_blog import create_app  # create_app関数を用いて、アプリケーションを作成してスクリプトを実行

from flask_blog.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(create_app)
    manager.add_command('init_db', InitDB())
    manager.run()
