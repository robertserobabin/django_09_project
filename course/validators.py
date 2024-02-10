import re

from rest_framework.serializers import ValidationError


class Validator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('sdaf')
        tmp_val = dict(value).get(self.field)
        if bool(reg.match(value)):
            raise ValidationError('TooBad')
