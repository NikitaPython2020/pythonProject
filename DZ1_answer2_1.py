from itertools import combinations

rostel_string = 'Ростелеком'

matchRostelecom = 0

for i in range(len(rostel_string)):
    list_rostel = list(combinations(rostel_string,i))
    print(len(list_rostel))
    stats = {}
    with open('C:/users/user/Desktop/Нетология/01. Подготовка/DZ1/RUS.txt','r') as f:
        for line in f:
            line = line.strip()
            for cur_list_rostel in list_rostel:
                if (''.join(cur_list_rostel)) == line:
                    print(line)
                    print(' ',''.join(cur_list_rostel))
                    matchRostelecom += 1
print('Итого найдено слов, составленых из слова Ростелеком: ', matchRostelecom)
