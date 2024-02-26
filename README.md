Главный эндпоинт с получением погоды и обновлением баланса
http://127.0.0.1:5000/update_balance_by_weather?userId=(Указать ID пользователя)&city=(Город для получения погоды)




Ссылки для разных городов по которым можно произвести нагрузочное тестирование
http://127.0.0.1:5000/update_balance_by_weather?userId=4&city=Minsk
http://127.0.0.1:5000/update_balance_by_weather?userId=4&city=Moscow
http://127.0.0.1:5000/update_balance_by_weather?userId=4&city=New%20York
http://127.0.0.1:5000/update_balance_by_weather?userId=4&city=London
http://127.0.0.1:5000/update_balance_by_weather?userId=4&city=Tokyo





Доступные эндпоинты для получения списка юзеров, также изменение и удаление
http://127.0.0.1:5000/user/<int:user_id>
http://127.0.0.1:5000/del_user/<int:user_id>
http://127.0.0.1:5000/users
