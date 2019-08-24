import requests

from config import api_url


def data(left_operand, operation, right_operand):
    json_data = {
        "left_operand": left_operand, "operation": operation,
        "right_operand": right_operand
    }
    return json_data


def request_post(json):
    request = requests.post(api_url(), json=json)
    return request
