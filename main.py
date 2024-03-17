# def even_nambers(list) -> list:
#     new_list = []

#     for i in list:
        
#         if i %2 == 0:
        
#             new_list.append(i)
#     return new_list    

# print(even_nambers([1, 2, 4, 5]))


# [1, 2, 3], [a, b, c] -> [1, a, 2, b, 3, c]

def one_list_from_two(list_1, list_2):
    
    counter = 0
    main_list = []
    for i in list_1:
        
        main_list.append(list_1[counter])
        main_list.append(list_2[counter])
        counter += 1
    return main_list

print(one_list_from_two([1, 2, 3], ['a', 'b', 'c']))