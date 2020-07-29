from application import app
from flask import render_template, request
import requests
import random
from flask_sqlalchemy import SQLAlchemy
import os

app.config['SECRET_KEY'] = os.getenv('LOOT_SECRETKEY')
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASS')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DBNAME')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
#                                         os.getenv('SQL_USER') + \
#                                         ':' + \
#                                         os.getenv('SQL_PASS') + \
#                                         '@' + \
#                                         os.getenv('SQL_HOST') + \
#                                         ':' + \
#                                         os.getenv('SQL_PORT') + \
#                                         '/' + \
#                                         os.getenv('SQL_DBNAME')

db = SQLAlchemy(app)

class loot_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loot_result = db.Column(db.String, nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Loot: ' + self.loot_result + '\n'
                'ID: ' + str(self.id)
            ]
        )

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    print(response)
    sentence = response.text
    # loot_data = loot_table(
    #     loot_result=sentence
    # )
    # db.session.add(loot_data)
    # db.session.commit()
    return render_template('index.html', sentence = sentence, title = 'Home')
