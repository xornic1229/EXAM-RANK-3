def inter(s1: str, s2: str) -> str:
    result = ""

    for char in s1:
        if char in s2 and char not in result:
            result += char

    return result