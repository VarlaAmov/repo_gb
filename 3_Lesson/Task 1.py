dict = {"one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"}

def num_translate(number):
        for key, value in dict.items():
                if number == key:
                        return value

print(num_translate("four"))
print(num_translate("ten"))
print(num_translate("chto-to"))


