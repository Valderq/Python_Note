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
length_sum = 3
count = 3
while length_sum < input_number:
    number_list.append(number_list[count-3]+number_list[count-2])
    length_sum = length_sum + len(str(number_list[count]))
    count = count + 1

count -= 1
if abs(length_sum - input_number) >= abs((length_sum - len(str(number_list[count]))) - input_number):
    number_list = number_list[:-1]





if __name__ == "__main__":
    digit_count = 0
    for i in number_list:
        digit_count += len(str(i))

    print(
        f"digit_count = {digit_count}\n"
        f"{number_list}\n"
    )
