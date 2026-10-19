import re
from django.core.exceptions import ValidationError


def validate_positive_price(value):
    """
    Власний валідатор (В5.3):
    Перевіряє, що ціна квітки є додатнім числом.
    Повідомлення про помилку українською мовою.
    """
    if value is not None and value <= 0:
        raise ValidationError(
            "Ціна квітки повинна бути більшою за 0 грн.",
            code="invalid_price",
        )


def validate_latin_name(value):
    """
    Власний валідатор для ботанічної назви (В5.3):
    Дозволяє лише латинські літери, пробіли, дефіси та крапки.
    """
    if value and not re.match(r"^[A-Za-z\s\.\-]+$", value):
        raise ValidationError(
            "Ботанічна назва повинна містити лише символи латинського алфавіту (наприклад: 'Paeonia lactiflora').",
            code="invalid_latin_name",
        )


def validate_phone_ua(value):
    """
    Власний валідатор для форми консультації (В5.2, В5.3):
    Перевіряє формат українського номера телефону.
    """
    pattern = r"^(\+38)?0\d{9}$"
    clean_val = re.sub(r"[\s\-\(\)]", "", value)
    if not re.match(pattern, clean_val):
        raise ValidationError(
            "Введіть коректний номер телефону у форматі +380XXXXXXXXX або 0XXXXXXXXX.",
            code="invalid_phone_ua",
        )
