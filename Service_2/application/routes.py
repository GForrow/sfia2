from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def beginning():

	list = ['Common','Common','Common','Common','Common','Common','Common','Common','Rare','Rare','Rare','Rare','Epic','Epic','Legendary']
	
	return list[random.randrange(15)]