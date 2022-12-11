from project import *
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("cs411-8a6c8-firebase-adminsdk-t4if4-97973a0a37 (1).json")

db = firestore.client()
doc_ref = db.collection(u'users')

try:
    docs = doc_ref.get()
    for doc in docs:
        print(u'Doc Data:{}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')
    
def upload(db,username,password,email,item,name):
    doc_ref = db.collection(username).document(password)
    doc_ref.set({u'email':email , u'item':item , u'name':name})



