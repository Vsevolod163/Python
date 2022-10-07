# Напишите программу, удаляющую из текста все слова, содержащие "абв"


def delete_words(word, list):

    result_list = []

    for i in range(len(list)):
        if word not in list[i]:
            result_list.append(list[i])
    
    return result_list

string1 = 'Вот мойабв итоговый абвгд результат'
word = 'абв'

list1 = string1.split()

result = delete_words(word, list1)
print(result)