import requests

from helpers.config import api_url


class Test:
    def test_request(self):
        json_data = {"left_operand": 3, "operation": "+", "right_operand": 2}

        request = requests.post(api_url(), json=json_data)
        response = request.json()['result']

        assert response == 5, 'Неправильный результат'
