"""
Input 3 digits, abc
the fourth one is a+b, fifth is b+c, sixth is c+(a+b)...
find a list fit line-3 with 100*a+10*b+c numbers
"""


input_number = int(input("Enter:"))

digit_3 = input_number % 10
digit_2 = input_number // 10 % 10
digit_1 = input_number // 100
number_list = [digit_1, digit_2, digit_3]

for i in range(3,input_number):
    number_list.append(number_list[i-3]+number_list[i-2])



if __name__ == "__main__":
    print(
        f"number of elements: {len(number_list)}\n"
        f"{number_list}"
    )
