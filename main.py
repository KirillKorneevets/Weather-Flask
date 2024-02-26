from flask import Flask
from endpoint import list_users, update_balance, update_username, delete_user
from db_config import db
from users_config import create_users



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


create_users(app)


app.add_url_rule('/update_balance_by_weather', 'update_balance', update_balance, methods=['GET'])
app.add_url_rule('/users', 'list_users', list_users, methods=['GET'])
app.add_url_rule('/user/<int:user_id>', 'update_username', update_username, methods=['PUT'])
app.add_url_rule('/del_user/<int:user_id>', 'delete_user', delete_user, methods=['DELETE'])



if __name__ == '__main__':
    app.run()



