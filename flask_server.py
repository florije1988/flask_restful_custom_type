# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, request, jsonify
from flask.ext import restful
from flask_restful import reqparse
from marshmallow import Schema, fields, pprint, ValidationError


app = Flask(__name__)
api = restful.Api(app)


# class ValidateSets(object):
#
# def __init__(self, name):
# self.name = name
#
# def __call__(self, value):
#         if not value:
#             raise ValidationError('name must not be blank.')
#
#         return value
#
#     @staticmethod
#     def validate_name(name):
#         if not name:
#             raise ValidationError('name must not be blank.')


class UserSchema(Schema):
    name = fields.String()


class ArtistSchema(Schema):
    title = fields.String()
    artist = fields.Nested(UserSchema, many=True)


@ArtistSchema.validator
@UserSchema.validator
def validate_numbers(schema, input_data):
    if not input_data['name']:
        raise ValidationError('name must not be blank.')
    if not input_data['name']:
        raise ValidationError('name must not be blank.')


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

        result, errors = ArtistSchema().load(json_data)

        if errors:
            raise Exception("json error: %r" % result.errors)

        return jsonify(result)


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)