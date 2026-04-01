import unittest
from unittest.mock import Mock, patch
import weather_service


class TestWeatherService(unittest.TestCase):
    def test_get_weather_success(self):
        mock_data = {"city": "London", "temp": 25, "condition": "sunny", "humidity": 60}
        with patch("weather_service.api_client.fetch_weather_data", return_value=mock_data):
            result = weather_service.get_weather("London")
            self.assertEqual(result["temp"], 25)
            self.assertEqual(result["condition"], "sunny")

    def test_get_weather_api_error(self):
        with patch("weather_service.api_client.fetch_weather_data", side_effect=Exception("API error")):
            with self.assertRaises(Exception):
                weather_service.get_weather("London")

    def test_get_weather_timeout(self):
        with patch("weather_service.api_client.fetch_weather_data", side_effect=TimeoutError("Timeout")):
            with self.assertRaises(TimeoutError):
                weather_service.get_weather("London")

    @patch("weather_service.api_client.fetch_forecast")
    def test_get_forecast_with_patch(self, mock_fetch):
        mock_fetch.return_value = [
            {"day": 1, "temp": 20, "condition": "sunny"},
            {"day": 2, "temp": 22, "condition": "cloudy"},
        ]
        result = weather_service.get_forecast("Paris", days=2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["temp"], 20)
        mock_fetch.assert_called_once_with("Paris", 2)

    @patch("weather_service.api_client.get_current_hour", return_value=8)
    def test_greeting_morning(self, mock_hour):
        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good morning")

    @patch("weather_service.api_client.get_current_hour", return_value=14)
    def test_greeting_afternoon(self, mock_hour):
        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good afternoon")


if __name__ == "__main__":
    unittest.main()
