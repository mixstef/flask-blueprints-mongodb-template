from flask import Blueprint
from pymongo import ReturnDocument

from ..app import mongo


hello = Blueprint('hello',__name__)


@hello.route('/')
def index_page():
	record = mongo.db.users.find_one_and_update({'user':'anonymous'},
				                    {'$inc':{'visits':1},
				                     '$set':{'user':'anonymous'}
				                    },upsert=True,
				                    return_document=ReturnDocument.AFTER)
	return 'Hello anonymous! You have visitied this page {} times!'.format(record['visits'])
	
