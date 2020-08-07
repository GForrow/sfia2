from application import app
import requests


@app.route('/randomword', methods=['GET'])
def item():
    beginning = requests.get('http://Service_2:5001/randomphrase')
    ending = requests.get('http://Service_3:5002/randomphrase')
    response = beginning.text + " " + ending.text
    return response