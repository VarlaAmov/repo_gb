# import re
#
# re1 = re.compile(r"""(?P<username>(?:[A-z]{4}\d+[_'.+\-]\w+)|(?:\w{4,8}))@   #ИМЯ
#                      (?P<domain>[a-z]+(?:\.[a-z]+(?:\.|)[a-z]+|\d+\w+\.\w+|-[a-z]+\.\w+))   #ДОМЕН
#                      """, re.VERBOSE)
#
#
# def email_parse(email_address, i=None):
#     rez = re1.finditer(email_address)
#     for i in rez:
#         return i.groupdict()
#     try:
#         if i == None:
#             msg = f'wrong email: {email_address}'
#             raise ValueError(msg)
#     except ValueError:
#         raise
#
# print(email_parse('name@doenname12.ru'))
# print(email_parse('na23me@doenname.ru'))
# print(email_parse('na_me@doenname.ru'))
#
# print(email_parse('name@do!enname.ru'))
#


def sum(numbers):
    result = 0
    for num in numbers:
        result += num

    return result

sum("12345")  # 15