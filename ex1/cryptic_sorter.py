def cryptic_sorter(strings: list[str]) -> list[str]:
    def count_vowels(word: str) -> int:
        count = 0

        for char in word.lower():
            if char in "aeiou":
                count += 1

        return count

    def sort_key(word: str):
        return (
            len(word),
            word.lower(),
            count_vowels(word),
            word
        )

    return sorted(strings, key=sort_key)