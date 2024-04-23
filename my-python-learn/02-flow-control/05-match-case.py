x = 4

match x:
    case 1 | 4:
        print("1 or 4")
    case 2:
        print("2")
    case 3:
        print("3")
    case 4:
        print("4")
    case 5:
        print("5")
    case _:
        print("default")


lst = ['A', 'B', 'C']

match lst:
    case ['A', 'B']:
        print("1 or 4")
    case ['C']:
        print("2")
    case ['A', 'B', 'C']:
        print("3")
    case _:
        print("default")


class ATMCnost:
    DEP = 1
    WITH = 2
    BAL_C = 3

option = 3
print("ATMCnost")
match option:
    case ATMCnost.DEP:
        print("1 or 4")
    case ATMCnost.WITH:
        print("2")
    case ATMCnost.BAL_C:
        print("3")
    case _:
        print("default")