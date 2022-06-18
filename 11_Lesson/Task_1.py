class DateInitError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DataClass():
    def __init__(self, str1):
        string2 = self.data_to_int(str1)
        if DataClass.check_date_value(string2):
            self.date_list = string2
        else:
            raise DateInitError("Incorrect input value")

    @classmethod
    def data_to_int(cls, data_string):
        try:
            int_list = data_string.split('-')
            int_list = [int(a) for a in int_list]
            return int_list
        except ValueError as e:
            raise DateInitError("Incorrect input format")

    @staticmethod
    def check_date_value(list1):
        return len(list1) == 3 and 1 <= list1[0] <= 31 and 1 <= list1[1] <= 12 and 1 <= list1[2]

    def __str__(self):
        return f'{self.date_list[2]}.{self.date_list[1]}.{self.date_list[0]}'


print('\n\tThe program read dates , validate them and print in requested format.')
print('\tIn case input can not be validated, the exception rised. \n')

lst_date = [
    "31-12-2021",
    "32-12-2022",
    "12-12--2022"
        ]

for el in lst_date:
    try:
        dat1 = DataClass(el)
        print(f'for input:  {el} object created : {dat1} ')
        print(f'for input:  {el} printout result : {dat1} \n')
    except DateInitError as e:
        print(f'for input:  {el} result : {e}\n')





