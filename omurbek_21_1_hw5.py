import re


class ValidCarNumber:
    def __init__(self, number = input("input:")):
        self.number = number

    def is_valid(self):
        is_number = re.search(r'([0-9]{2})KG([0-9]{3})([A-Z]{3})', self.number)
        try:
            if self.number[is_number.start():is_number.end()] == self.number:
                return f"Its valid number"
        except:
            return f"its InValid number"


bmw = ValidCarNumber()
print(bmw.is_valid())