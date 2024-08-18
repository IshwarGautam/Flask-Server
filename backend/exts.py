from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
To create a db:
1. set FLASK_APP=main.py
2. flask shell
2.1 db.create_all()
"""