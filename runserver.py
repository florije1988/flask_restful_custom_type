# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

import datetime as dt
from datetime import date
from marshmallow import Schema, fields, pprint, ValidationError


class User(object):
    def __init__(self, name, email, age=None):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()
        self.friends = []
        self.employer = None
        self.age = age

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


def validate_name(name):
    if not name:
        raise ValidationError('name must not be blank.')


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()


class ArtistSchema(Schema):
    name = fields.String(validate=validate_name)


class AlbumSchema(Schema):
    title = fields.String(validate=validate_name)
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema)


class ValidatedUserSchema(UserSchema):
    name = fields.String(validate=validate_name)
    age = fields.Number(validate=lambda n: 18 <= n <= 40)


if __name__ == '__main__':
    user_data = {
        'created_at': '2014-08-11T05:26:03.869245',
        'email': u'ken@yahoo.com',
        'name': u'Ken'
    }
    schema = UserSchema()
    result = schema.load(user_data)
    pprint(result.data)

    in_data = {'name': '', 'email': 'mick@stones.com', 'age': 71}
    result = ValidatedUserSchema().load(in_data)
    pprint(result.errors)

    bowie = dict(name='')
    album = dict(artist=bowie, title='', release_date=date(1971, 12, 17))

    schema = AlbumSchema()
    result = schema.dump(album)
    pprint(result.data)
    print type(result.data)

    result = schema.load(result.data)
    pprint(result.errors)