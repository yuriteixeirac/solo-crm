import re


class NumberValidator:
    NUMBER_PATTERN = re.compile(r'(\+?55)?\s?\(?[0-9]{2}\)?\s?9?[0-9]{4}(-?|\s?)[0-9]{4}')


    @staticmethod
    def validate(number: str) -> bool:
        if re.match(NumberValidator.NUMBER_PATTERN, number):
            return True
        return False
