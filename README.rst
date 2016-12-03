Simple Input Validator
====================================================

Simple Input Validator(SIV) validates input data by rules that developer defined

tutorial
----------
1. define your validator
::
    # coding: utf-8

    from siv.validator import Validator
    from siv.fields import IntegerField, StringField


    class RegisterValidator(Validator):
        age = IntegerField(require=True)
        name = StringField(max_length=5)
        mobile = IntegerField(max=5)
        email = EmailField(min_length=3, max_length=10)

