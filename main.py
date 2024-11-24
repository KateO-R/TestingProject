def count_vowels(s: str) -> int:
    """Функция для подсчёта количества гласных в строке."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


if __name__ == "__main__":
    # Пример использования
    example_string = "Hello, World!"
    print(f"Number of vowels in a string '{example_string}': {count_vowels(example_string)}")