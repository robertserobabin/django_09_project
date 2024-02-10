from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from urllib.parse import urlparse

class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        passed_tag = 'youtube.com'
        if self.field not in value or passed_tag not in value[self.field]:
            raise ValidationError(f'Only youtube link is allowed for the {self.field} field"')
