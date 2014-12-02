from gitut.settings import DATABASES

from django.db import connection
import os, sys
path = 'C:/Users/Jenkins/Desktop/GIT/app/gitut'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gitut.settings")

def setup_package():
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE gittut;')
 
def teardown_package():
    # cursor = connection.cursor()
    # cursor.execute('DROP DATABASE gittut;')