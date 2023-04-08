# This is a sample Python script.
from datetime import datetime, time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    char_list = [i for i in name]
    hex_name = [format(ord(i), "x") for i in char_list]
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {hex_name}')  # Press Ctrl+F8 to toggle the breakpoint.
    sp =list(name)
    print(sp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi("code")
    # print(round(7.4))
    # print(round(154752, -2))
    #
    # print([1,4,75,4,1].count(4))
    time = time(hour=16, minute=0)
    print(time)
# See PyCharm help at https://www.j etbrains.com/help/pycharm/
