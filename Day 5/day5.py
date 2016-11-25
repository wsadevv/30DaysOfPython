# Function
print("Function")
# function definition -> def NAME (parameter || empty)
def parse_lists(some_list):
    list_int = []
    list_str = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            list_int.append(i)
        elif isinstance(i, str):
            list_str.append(i)
        else:
            pass
    return list_int, list_str


def examples():
    str_list = ['aa', 'bb', 'cc', 'AA', 'BB', 'CC']

    print(str_list)

    str_list.sort()
    # maisculas primeiro - sem parâmetro de ordenação
    print(str_list)
    # lowercase  to uppercase
    str_list.sort(key=str.lower)
    print(str_list)

    str_list.sort(reverse=True)
    print(str_list)


def mySummoner(list_numbers):
    print(sum(list_numbers))

#Using Python have one crucial modification: First you define your methods 
#and then you define "main"

myList = [3.1415, "There", "was", "THE", "time", 1, 2, 3, 4]

print("MAIN")
print(parse_lists(myList))

list_numbers = [1, 2, 3, 4, 5, 6]
mySummoner(list_numbers)

