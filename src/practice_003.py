
para_list = []
"""
m = 99999
for num in range(1, m + 1):
    if str(num)[::-1] == str(num):
        abcba_list.append(num)

print(abcba_list)
"""

max_range = int(input('enter max range: '))
for i in range(max_range):

    """    
    original = i
    reverse = 0
    while original > 0:
        a = original % 10
        reverse = reverse * 10 + a
        original = original // 10

    if reverse == i:
        para_list.append(i)
    """

    count = 0
    a = i

    while a > 0:
        a = a // 10
        count += 1

    a = i
    while count > 1:
        _if_i = True
        if a // 10**(count - 1) == a % 10:
            a = (a - (a // 10**(count - 1) * 10**(count - 1))) // 10
            count = count - 2
        else:
            _if_i = False
            break

        if _if_i:
            para_list.append(i)

if __name__ == "__main__":
    print(para_list)