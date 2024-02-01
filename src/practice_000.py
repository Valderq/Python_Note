import math

prime_list = []
_max = 9999
number_list = [True for i in range(0, _max+1)]
# for i in range(0, _max+1):
#     print(f"{i}: {number_list[i]}")

#
# for i in range(2, _max+1):
#     _if_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             _if_prime = False
#             break
#
#     if _if_prime:
#         prime_list.append(i)

# number_list[0] = False
# number_list[1] = False
# number_list[2] = True
#
# for i in range(3, _max+1):
#     for j in range(2, i):
#         if i % j == 0:
#             number_list[i] = False
#             break
#
# for i in range(0, _max):
#     if number_list[i]:
#         prime_list.append(i)
#
# print(prime_list)

for i in range(2, _max+1):
    if number_list[i]:
        for j in range(2*i, _max+1, i):
            number_list[j] = False

for i in range(2, _max+1):
    if number_list[i]:
        prime_list.append(i)



if __name__ == "__main__":
    print(prime_list)
