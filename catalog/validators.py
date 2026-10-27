import re
from django.core.exceptions import ValidationError



def validate_latin_name(value):
   
    if value and not re.match(r"^[A-Za-z\s\.\-]+$", value):
        raise ValidationError(
            "Ботанічна назва повинна містити лише символи латинського алфавіту (наприклад: 'Paeonia lactiflora').",
            code="invalid_latin_name",
        )


def validate_phone_ua(value):
   
    pattern = r"^(\+38)?0\d{9}$"
    clean_val = re.sub(r"[\s\-\(\)]", "", value)
    if not re.match(pattern, clean_val):
        raise ValidationError(
            "Введіть коректний номер телефону у форматі +380XXXXXXXXX або 0XXXXXXXXX.",
            code="invalid_phone_ua",
        )
