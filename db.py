from tinydb import TinyDB, Query
db = TinyDB('db.json')

def makeNewUser(id):
  db.insert({'id': id, 'balance': 0})
  #send message welcoming?

#TODO 
# add a set, change, and delete

