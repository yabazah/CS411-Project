from project import *
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("cs411-8a6c8-firebase-adminsdk-t4if4-97973a0a37 (1).json")

#upload 
db = firestore.client()
doc_ref = db.collection(u'users')

try:
    docs = doc_ref.get()
    for doc in docs:
        print(u'Doc Data:{}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')
    
def upload(db,username,item):
    doc_ref = db.collection(u'users').document(username)
    doc_ref.set({'item':item  })
    


#retrieve 

def retrieve(username):
   collections = db.collection('users').document(username).collections()
   for collection in collections:
    for doc in collection.stream():
        print(f'{doc.id} => {doc.to_dict()}')
        
