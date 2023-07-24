romennum_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

input_num = input("Please enter the roman numeral you want to convert: ")


def roman_to_decimal(roman_numeral):
    result = 0
    prev_value = 0

    for letter in reversed(roman_numeral):
        value = romennum_dict[letter]

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result


if input_num.upper() == input_num and all(letter in romennum_dict for letter in input_num):
    decimal_num = roman_to_decimal(input_num)
    print(decimal_num)
else:
    print("Please enter a valid value")
