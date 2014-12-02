from gitut.settings import DATABASES

import MySQLdb as db

def setup_package():
    con = db.connect(host="localhost")
    cur = con.cursor()
    cur.execute('CREATE DATABASE gittut;')
 
def teardown_package():
    con = db.connect()
    cur = con.cursor()
    cur.execute('DROP DATABASE gittut;')