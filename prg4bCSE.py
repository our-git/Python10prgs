def roman2integer(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    pre_val = 0
    for symbol in roman_numeral[::-1]:
        value = roman_dict[symbol]
        if value >= pre_val:
            res = res + value
        else:
            res = res - value
        pre_val = value
    return res

roman_numeral = input("Enter a Roman numeral:")
integer_value = roman2integer(roman_numeral)
print("Integer value:", integer_value)
