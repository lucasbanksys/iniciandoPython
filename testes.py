from pprint import pprint

unsorted_list = [{"id": 0, "name": "User", "age": 30},
    {"id": 1, "name": "Another User", "age": 42},
    {"id": 2, "name": "Another User", "age": 25},
    {"id": 3, "name": "Yet Another User", "age": 30}]

sorted_list = sorted(unsorted_list, key=lambda t: t[0]) 
pprint(sorted_list)