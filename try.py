def change_list_item(index, new_value, my_list):
   try:
    my_list[index] = new_value
   except IndexError as index_err:
       print(f"Error ! Index out of range, list={my_list}, error={index_err}")
   finally:
       print(f"Method funished, list={my_list}")

def _change_list_item(index, new_value, my_list):
    my_list[index] = new_value

# _change_list_item(56, 'a', [9, 8, 7, 6, 5, 4, 3, 2, 1])
# change_list_item(4, 3333, [8,7,6])
# change_list_item(2, [1,2,3], [10, 3, 5, 4])

def convert_to_int(_str :str):
    try:
        a= int(_str)
        print(f"my int is {a}")
    except  Exception :
        print("I was here",Exception)


l = []
l.append(l)
print(l)