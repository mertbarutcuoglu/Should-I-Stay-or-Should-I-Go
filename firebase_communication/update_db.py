from firebase import Firebase
from .config import get_db, get_auth

auth = get_auth()
db = get_db()

def set_active(user):
    db.child('users').child(user).update({'is_active': True})

def set_deactive(user):
    db.child('users').child(user).update({'is_active': False})