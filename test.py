import pytest
from main import count_vowels

def test_all_vowels():
    """Проверка строки, содержащей только гласные."""
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    """Проверка строки, не содержащей гласных."""
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0

def test_mixed_string():
    """Проверка смешанной строки, содержащей как гласные, так и согласные, включая прописные и строчные буквы."""
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("PyThOn Is AwEsOmE") == 6

if __name__ == "__main__":
    pytest.main()