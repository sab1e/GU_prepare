import os


def print_directory_contents(sPath):
    """
        Функция принимает имя каталога и распечатывает его содержимое
        в виде «путь и имя файла», а также любые другие
        файлы во вложенных каталогах.

        Эта функция подобна os.walk. Использовать функцию os.walk
        нельзя. Данная задача показывает ваше умение работать с
        вложенными структурами.
        заполните далее

        Пример:
        [
        ('mainapp', 'admin.py'),
        ('mainapp\\management\\commands', 'seed_db.py'),
        ...
        ]
    """

    if os.path.isfile(sPath):
        return os.path.split(sPath)[1]
    else:
        directory_list = [sPath]
        directory_list.extend([print_directory_contents(
            os.path.join(sPath, element)) for element in os.listdir(sPath)])
        return directory_list


if __name__ == '__main__':
    current_path = '/home/'
    directory_list = print_directory_contents(current_path)
    for i in directory_list:
        print(i)
