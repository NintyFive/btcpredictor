import pyrebase
import os

class Database:

	fb = None
	rt = None
	db = None

	@staticmethod
	def connect():

		config = {
            "apiKey": "AIzaSyCDGL9scEavQTjKw4qHXEkrJpW5_pgiFEo",
            "authDomain": "btcpredictor-5ddba.firebaseapp.com",
            "databaseURL": "https://btcpredictor-5ddba-default-rtdb.firebaseio.com",
            "projectId": "btcpredictor-5ddba",
            "storageBucket": "btcpredictor-5ddba.appspot.com",
            "messagingSenderId": "798702128709",
            "appId": "1:798702128709:web:042e843e3d4adeb21f9d2c",
            "measurementId": "G-7SF3JXZZE2"
		}

		print('Connecting to databases... ', end='')
		Database.fb = pyrebase.initialize_app(config)
		Database.rt = Database.fb.database()
		Database.db = Database.fb.storage()
		print('done!')
