# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
dict1 = {"1":"0", "0":"1"}
lis = []

def hexiBinary(i):
    num = ""
    if i > 255:
        while (i > 0):
            if 10 > i%16 >= 0:
                num += str(i%16)
                i = int(i/16)
            elif 16> i%16 >= 10:
                num += dict[i%16]
                i = int(i/16)
        num2 = "".join(reversed(num))
        print(num2)
    elif i <= 255:
        while (i > 0):
            if i%2 == 1:
                lis.append(str(i%2))
                i = int(i/2)
            else:
                lis.append("0")
                i = int(i/2)
        j = 0
        while j < len(lis):
            if lis[j] == "0":
                lis[j] = "1"
                j = len(lis)
            else:
                lis[j] = "0"
                j = j + 1
        if len(lis) < 8:
            h = (8-len(lis))
            while h > 0:
                lis.append("0")
                h = h - 1
        lis.reverse()
        print("".join(lis))



hexiBinary(56)