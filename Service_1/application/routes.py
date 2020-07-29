from application import app
from flask import render_template, request
import requests
import random
from flask_sqlalchemy import SQLAlchemy
import os

app.config['SECRET_KEY'] = os.get('LOOT_SECRETKEY')
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        os.get('SQL_USER') + \
                                        ':' + \
                                        os.get('SQL_PASS') + \
                                        '@' + \
                                        os.get('SQL_HOST') + \
                                        ':' + \
                                        os.get('SQL_PORT') + \
                                        '/' + \
                                        os.get('SQL_DBNAME')

db = SQLAlchemy(app)

class Loot(db.Model):
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
    loot_data = Loot(
        loot_result=sentence
    )
    db.session.add(loot_data)
    db.session.commit()
    return render_template('index.html', sentence = sentence, title = 'Home')
