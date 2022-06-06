# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

def bubble_sort(my_list):
    swap = 0
    for i in range (len(my_list) - 1):
        swap = 0
        for j in range (len(my_list) - 1 - i):
            if my_list[j+1] < my_list[j]:
                my_list[j+1], my_list[j] = my_list[j], my_list[j+1],
                swap += 1
        if swap == 0:
            break
    return(my_list)


from random import randint

with open ("my_numbers.txt", "w") as file:
    for i in range (10):
        file.write(str(randint(0, 100)) + " ")
    file.write("\n")



with open ("my_numbers.txt", "r+") as file:
    incoming_list = [int(i) for i in file.readline().split()]
    bubble_sort(incoming_list)

    [file.write(str(i) + " ") for i in incoming_list]
    print(incoming_list)
    
    
