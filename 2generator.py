# Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())

import hashlib
import os


def generator():
    file_path = os.getcwd()
    with open(f'{file_path}/wiki_links.txt') as file:
        for line in file:
            hash_object = hashlib.md5(line.encode())
            hash_object = hash_object.hexdigest()
            yield hash_object

if __name__ =='__main__':
    for line_hashed in generator():
        print(line_hashed)
