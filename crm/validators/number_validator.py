import re


class NumberValidator:
    NUMBER_PATTERN = re.compile(r'^(\+?55)?\s?\(?[0-9]{2}\)?\s?9?[0-9]{4}(-?|\s?)[0-9]{4}$')


    @staticmethod
    def validate(number: str) -> bool:
        """Valida números brasileiros."""
        if re.match(NumberValidator.NUMBER_PATTERN, number):
            filtered_number = re.sub(r'\s|\-|\(|\)|\+', '', number)
            if not len(filtered_number) < 6:
                return True
        return False
