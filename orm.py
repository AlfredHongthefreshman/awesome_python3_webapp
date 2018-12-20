#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 排除Model类本身
        pass


class Model(dict, metaclass=ModelMetaclass):
    pass


class Field(object):
    pass


class StringField(Field):
    pass


class IntegerField(Field):
    pass
