def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not 2 <= from_base <= 36 or not 2 <= to_base <= 36:
        return "ERROR"

    number = number.upper()

    if number == "":
        return "ERROR"

    for char in number:
        if char not in digits[:from_base]:
            return "ERROR"

    decimal = int(number, from_base)

    if decimal == 0:
        return "0"

    result = ""

    while decimal > 0:
        remainder = decimal % to_base
        result = digits[remainder] + result
        decimal //= to_base

    return result