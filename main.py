from math import sqrt
"""
Sort the list by item length in ascending and descending order.
 sort_me = ["Kaunas", "Vilnius", 
 "Alytus", "Klaipeda", "Varena", "Druskininkai", "Klaipeda"]
"""
def antras():
    sort_me = ["Kaunas", "Vilnius",
               "Alytus", "Klaipeda", "Varena", "Druskininkai", "Klaipeda"]
    sorted_list = sorted(sort_me, key=len)

    print(sorted_list)
    print(sorted_list[::-1])
antras()

"""
Perform list element transformation: 
1. by using formula: x = x * (x - 10), 2. square each element.
 my_list = [12, 45, 23, 56, -546, 34]
"""
def trecias():
    my_list = [12, 45, 23, 56, -546, 34]
    first = []
    second = []
    for my in my_list:
        print(my)
        x = my * (my - 10)
        y = my * my
        first.append(x)
        second.append(y)
    print(first)
    print(second)

trecias()