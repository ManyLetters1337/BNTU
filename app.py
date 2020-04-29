"""
App
"""
from create_app import create_app

db_url = 'mysql+pymysql://admin:LolKek1337@localhost/bntu'
app = create_app(db_url, False)     # Change to True
