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
