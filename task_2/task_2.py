from typing import Callable, Generator
import re


def generator_numbers(input_text: str) -> Generator:
    """Creates generator numbers based on input text."""
    pattern = r"\b\d+\.\d+\b"
    numbers = re.findall(pattern=pattern, string=input_text)
    for number in numbers:
        yield float(number)


def sum_profit(input_text: str, func: Callable) -> float:
    """Returns the sum of all numbers found in text."""
    return sum(func(input_text))


if __name__ == "__main__":
    text = ("The total income of the employee consists of several parts: 1000.01 as the main income, "
            "supplemented by additional income of 27.45 and 324.00 dollars.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Total income: {total_income}")
