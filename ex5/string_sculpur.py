def string_sculptor(text: str) -> str:
    result = ""
    count = 0

    for char in text:
        if char.isalpha():
            if count % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
            count += 1
        else:
            result += char

    return result