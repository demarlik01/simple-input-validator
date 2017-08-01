Simple Input Validator
====================================================

Simple Input Validator(SIV) validates dict by rules that developer defined

Tutorial
----------
1. define your validator
::
    from siv.validator import Validator
    from siv.fields import IntegerField, StringField


    class RegisterValidator(Validator):
        age = IntegerField(require=True)
        name = StringField(max_length=5)
        mobile = IntegerField(max=5)
        email = EmailField(min_length=3, max_length=10)

2. Use it
:: 
    
    @app.route("/join", methods=['POST'])
    def join():
        validator = RegisterValidator()
        json_dict = json.loads(request.data)
        if not validator.validate(json_dict):
            return str(validator.error)
        return "success"
