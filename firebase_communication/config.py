from firebase import Firebase
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": ""
}

firebase = Firebase(config)
auth = firebase.auth()
db = firebase.database()

def get_db():
    return db


def get_auth():
    return auth
