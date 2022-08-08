def convert(n):
    if n > 1:
        convert(n // 2)
    print(n % 2, end='')


num = int(input("please enter any number"))

convert(num)
