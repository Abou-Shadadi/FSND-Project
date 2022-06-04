import os
import psycopg2 # connect to db
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
conn = psycopg2.connect(host='localhost',
                            database='fyyur_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:naslab123@localhost/fyyur_db'
