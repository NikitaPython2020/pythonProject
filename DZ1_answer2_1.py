from itertools import combinations

matchRostelecom = 0

for i in range(10):
    list_rostel = list(combinations('Ростелеком',i))
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
print('Итого найдено слов с Ростелеком вхождений: ', matchRostelecom)
