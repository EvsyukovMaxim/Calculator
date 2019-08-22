from helpers.request import data, request_post


def plus(a, b):
    response = request_post(json=data(a, '+', b)).json()['result']
    return response


def minus(a, b):
    z = a - b
    return z
