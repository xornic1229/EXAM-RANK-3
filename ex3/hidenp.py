def hidenp(small: str, big: str) -> bool:
    i = 0

    for char in big:
        if i < len(small) and char == small[i]:
            i += 1

    return i == len(small)