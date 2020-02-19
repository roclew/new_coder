"""
约瑟夫环
"""


def get_list():
    persons = ["1"] * 15
    persons.append("0")
    for i in range(1, 14):
        persons.insert(-9, "0")
        for i in persons:
            print(i, end="")
        print()
        persons = persons[-9:] + persons[:-9]
    for i in persons[-9:]+persons[:-9]:
        print(i,end="")
    return persons


def main():
    get_list()


if __name__ == "__main__":
    main()