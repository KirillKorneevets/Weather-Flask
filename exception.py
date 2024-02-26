class WeatherDataError(Exception):
    """Исключение возникающее при некорректных или недоступных данных о погоде."""

    def __init__(self, message="Weather data is not available or invalid"):
        self.message = message
        super().__init__(self.message)