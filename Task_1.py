# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя


def increasing_list (incoming_list):
    length_of_sequence = [1]*len(incoming_list)
    for i in range (1, len(incoming_list)):
        for j in range (i):
            if incoming_list[i] > incoming_list[j] and length_of_sequence[i] < length_of_sequence[j] + 1:
                length_of_sequence[i] = length_of_sequence[j] + 1
    max_index = length_of_sequence.index(max(length_of_sequence))
    result = []
    for i in range (max_index, -1, -1):
        if max_index - length_of_sequence[i] == 1:
            result.append(incoming_list[i])
            max_index = max_index - 1
            
    return result[::-1]

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
print (increasing_list(my_list))
        