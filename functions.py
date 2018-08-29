def square(x):
    return x * x


for i in range(10):
    print(f"{i} squared is {square(i)}")
    # Older way to write formatted string on Python version 2.7 is
    # print("{} squared is {}".format(i, square(i)))
