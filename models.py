from db_config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Integer, nullable=False)


    def __init__(self, username, balance):
        """
        Инициализирует нового пользователя с заданными именем и балансом.
        """
        self.username = username
        self.balance = balance

    def add_user(self):
        """
        Добавляет пользователя в базу данных.
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_balance(cls, user_id, new_balance):
        """
        Обновляет баланс пользователя по его ID.
        Возвращает True при успешном обновлении, иначе False.
        """
        user = cls.query.get(user_id)
        if user:
            user.balance = new_balance
            db.session.commit()
            return True
        return False

    @classmethod
    def update_user(cls, user_id, username=None, balance=None):
        """
        Обновляет имя или баланс пользователя по его ID.
        """
        user = cls.query.get(user_id)
        if user:
            if username:
                user.username = username
            if balance is not None:  
                user.balance = balance
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_user(cls, user_id):
        """
        Удаляет пользователя по его ID.
        """
        user = cls.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
