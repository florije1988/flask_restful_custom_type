# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, request, jsonify
from flask.ext import restful
from flask_restful import reqparse
from marshmallow import Schema, fields, pprint, ValidationError


app = Flask(__name__)
api = restful.Api(app)


def validate_name(name):
    if not name:
        raise ValidationError('name must not be blank.')


class UserSchema(Schema):
    name = fields.String(validate=validate_name)


class ArtistSchema(Schema):
    title = fields.String(validate=validate_name)
    artist = fields.Nested(UserSchema, many=True)


def odd_number(value, name):
    if value % 2 == 0:
        raise ValueError("The parameter '{}' is not odd. You gave us the value: {}".format(name, value))

    return value


class HelloWorld(restful.Resource):
    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('OddNumber', type=odd_number, location='json')
        # args = parser.parse_args()
        # return {'hello': args.OddNumber}
        if not request.data:
            raise Exception("not request.data error!")

        json_data = request.get_json()

        result = ArtistSchema().load(json_data)

        if result.errors:
            raise Exception("json error: %r" % result.errors)

        return jsonify(result.data)


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)