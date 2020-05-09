import os


def adloader(num, cls):
    if num == 1:
        print(os.system("cd"))
        print("do clearing")
    elif num == 2:
        print("do enrolling")
    else:
        print("do recording "+cls)
