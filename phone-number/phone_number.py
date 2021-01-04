import re


class PhoneNumber:
    def __init__(self, number):
        self.number = re.sub(r'[^0-9]', '', number)
        #
        if len(self.number) == 11 and self.number[0] == '1':
            self.number = self.number[1:]

        if len(self.number) != 10 or self.number[0] in ['0', '1'] or self.number[3] in ['0', '1']:
            raise ValueError('Invalid phone number format.')

        self.area_code = self.number[0:3]

    def pretty(self):
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}'
