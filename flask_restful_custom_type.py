# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

from flask import Flask
from flask.ext import restful
from flask_restful import reqparse

app = Flask(__name__)
api = restful.Api(app)


def odd_number(value, name):
    if value % 2 == 0:
        raise ValueError("The parameter '{}' is not odd. You gave us the value: {}".format(name, value))

    return value


class HelloWorld(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('OddNumber', type=odd_number, location='json')
        args = parser.parse_args()
        return {'hello': args.OddNumber}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
