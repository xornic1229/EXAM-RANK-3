def echo_validator(text: str) -> bool:
    clean_text = ""

    for char in text:
        if char.isalpha():
            clean_text += char.lower()

    return clean_text != "" and clean_text == clean_text[::-1]