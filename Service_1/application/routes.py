from application import app
from flask import render_template, request
import requests
import random
from flask_sqlalchemy import SQLAlchemy
import os
from os import environ

app.config['SECRET_KEY'] = environ.get('LOOT_SECRETKEY')
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False
# app.config['MYSQL_HOST'] = os.getenv('SQL_HOST')
# app.config['MYSQL_USER'] = os.getenv('SQL_USER')
# app.config['MYSQL_PASSWORD'] = os.getenv('SQL_PASS')
# app.config['MYSQL_DB'] = os.getenv('SQL_DBNAME')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASS') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DBNAME')

db = SQLAlchemy(app)

class loot_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loot_result = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "".join(
            [
                'Loot: ' + self.loot_result + '\n'
                'ID: ' + self.id
            ]
        )

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    print(response)
    item = response.text
    loot_data = loot_table(
        loot_result=item
    )
    print(loot_data)
    db.session.add(loot_data)
    db.session.commit()
    return render_template('index.html', item = item, title = 'Home')

# @app.route('/create')
# def create():
#     db.create_all()
#     return "Added table and populated with dummy records"