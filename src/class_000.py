# import test

print("Hello!")     # print() for print something into terminal
print("class 000 name varible: ", __name__)
variable_input = input("Write anything you want")    # variable_input is a variable take the input data from user
                                                     # input() wait for user input into terminal and end when catch "Enter" sign
print(variable_input)    # using print() to output variable_input into terminal
if __name__ == "__main__":  # if __name__ has value "__main__", which represents the file is compiled as the first one.
    # if the file is main class in a compile, below will be exceeded.
    print('I am main file!')