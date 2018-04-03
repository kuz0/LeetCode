def rm_blank(string):
    lst = []
    for i in string:
        if i == " ":
            lst.append("-")
        elif i.isupper():
            lst.append(i.lower())
        else:
            lst.append(i)
    print("".join(lst))


if __name__ == '__main__':
    s = input("Enter: ")
    rm_blank(s)
