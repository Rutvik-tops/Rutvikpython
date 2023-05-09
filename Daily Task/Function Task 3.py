#WAP to print 1 to 10 without using loop


def print_num(num):
    if num <= 10:
        print(num)
        print_num(num+1)

print_num(1)
