from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_minsk(self):
        self.client.get("/update_balance_by_weather?userId=4&city=Minsk")

    @task
    def test_moscow(self):
        self.client.get("/update_balance_by_weather?userId=4&city=Moscow")

    @task
    def test_new_york(self):
        self.client.get("/update_balance_by_weather?userId=4&city=New%20York")

    @task
    def test_london(self):
        self.client.get("/update_balance_by_weather?userId=4&city=London")

    @task
    def test_tokyo(self):
        self.client.get("/update_balance_by_weather?userId=4&city=Tokyo")
