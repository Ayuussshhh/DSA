# It is an example of linear search algorithm (BASIC)

def linear_search ( list , target):
    for i in range ( 0 , len(list)):
        if list[i] == target:
            return i
        else:
            return None

def check(index):
    if index is not None:
        print("The value at the index is :" , index)
    else:
        print("The value is not found for that index")

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
num1 = int(input("Enter the Number whose indexing you want to find\n"))
check(linear_search( numbers , num1))

