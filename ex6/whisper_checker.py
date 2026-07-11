def whisper_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char

    return result
