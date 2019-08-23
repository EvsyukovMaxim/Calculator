from helpers.request import data, request_post


def plus(a, b):
    response = request_post(json=data(a, '+', b)).json()['result']
    return response


def minus(a, b):
    response = request_post(json=data(a, '-', b)).json()['result']
    return response


def multiply(a, b):
    response = request_post(json=data(a, '*', b)).json()['result']
    return response


def divide(a, b):
    response = request_post(json=data(a, '/', b)).json()['result']
    return response


def any_op(a, b, operation):
    response = request_post(json=data(a, operation, b)).json()['error']
    return response
