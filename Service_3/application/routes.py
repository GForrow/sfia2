from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def ending():

	list = ['Boots','Boots','Helm','Gloves','Gloves','Chest Piece','Shoulders','Legs','Amulet','Ring']
	
	return list[random.randrange(10)]