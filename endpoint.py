from flask import request, jsonify
from db_config import db
from models import User
from weather_request import fetch_weather
from exception import WeatherDataError


def update_balance():
    """
    Обновляет баланс пользователя на основе текущей температуры в указанном городе.
    Баланс увеличивается на значение температуры если она положительная,
    и уменьшается если отрицательная. Возвращает JSON с сообщением
    об успешном обновлении, новым балансом и температурой. В случае ошибок возвращает соответствующие
    сообщения об ошибках.
    """
    
    user_id = request.args.get('userId')
    city = request.args.get('city')

    try:
        temperature = fetch_weather(city)
    except WeatherDataError as e:
        return jsonify({'message': str(e)}), 500

    if temperature is None:
        return jsonify({'message': 'Failed to fetch weather data'}), 500

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if temperature > 0:
        balance_change = temperature
    else:
        balance_change = -temperature

    new_balance = user.balance + balance_change

    if new_balance < 0:
        return jsonify({'message': 'Balance cannot be negative'}), 400
    
    user.balance = new_balance
    db.session.commit()

    return jsonify({'message': 'Balance updated successfully', 'new_balance': new_balance, 'temperature': temperature})



def update_username(user_id):
    """
    Обновляет имя пользователя на основе предоставленного ID и нового имени.
    Принимает ID пользователя и новое имя из параметров запроса.
    Возвращает JSON-ответ с сообщением о результате операции.
    """
    data = request.json
    new_username = data.get('newusername')

    if not new_username:
        return jsonify({'message': 'New username is required'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user.username = new_username
    db.session.commit()

    return jsonify({'message': 'Username updated successfully', 'userId': user_id, 'newusername': new_username})


def delete_user(user_id):
    """
    Удаляет пользователя из базы данных по предоставленному ID пользователя.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully', 'userId': user_id})









def list_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({'id': user.id, 'username': user.username, 'balance': user.balance})
    return jsonify(users_list)