from db_config import db
from models import User

def create_users(app):
    with app.app_context():
        db.create_all()
        if User.query.count() == 0:  
            users = [
                User(username="user1", balance=5001),
                User(username="user2", balance=6000),
                User(username="user3", balance=7000),
                User(username="user4", balance=8000),
                User(username="user5", balance=9000),
            ]
            for user in users:
                db.session.add(user)
            db.session.commit()