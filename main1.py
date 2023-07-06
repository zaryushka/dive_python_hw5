# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def link_split(link):
    parts_1 = link.rsplit('/', 1)
    parts_2 = parts_1[1].split('.')

    path_link = parts_1[0]
    file_name_link = parts_2[0]
    file_ext_link = parts_2[1]
    return path_link, file_name_link, file_ext_link



link = 'https://luxe-host.ru/wp-content/uploads/d/3/1/d3172b9c4b179a06817b882b43f57f7d.jpeg'
print(link_split(link))

