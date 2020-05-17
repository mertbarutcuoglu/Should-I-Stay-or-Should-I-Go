from firebase import Firebase
from .config import get_db, get_auth

auth = get_auth()
db = get_db()

def create_account(email, password, name, max_people):
    
    user = auth.create_user_with_email_and_password(email, password)

    data = {
    "name": name,
    "max_people": max_people,
    "is_active": False,
    "current_people": 0,
    "total_people": 0
    }

    results = db.child("users").push(data, user['idToken'])
    active_user = results['name']
    return active_user

def login_user(email, password):
    user = auth.sign_in_with_email_and_password(email, password)
    return user

