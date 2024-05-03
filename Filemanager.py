import os
import shutil

class FileManager:
    def __init__(self):
        # Узнаём директорию из конфига и переходим в неё
        with open('D:\Projects\FIN_UN\Practice\sem4\config.txt', 'r') as file:
            workspace = file.readline()
            print(workspace)

        self.workspace = workspace
        os.makedirs(workspace, exist_ok=True)
        os.chdir(workspace)

    def cd(self, name):
        # Создание новой директории, если не существует
        try:
            os.mkdir(name)
            print(f"Директория '{name}' создана.")
        except FileExistsError:
            print(f"Директория '{name}' уже существует.")

    def dd(self, name):
        # Удаление директории
        try:
            os.rmdir(name)
            print(f"Директория '{name}' удалена.")
        except FileNotFoundError:
            print(f"Директория '{name}' не найдена.")
        except OSError:
            print(f"Директория '{name}' не пустая. Сначала удалите содержимое.")

    def lc(self):
        # Список файлов в директории
        contents = os.listdir()
        for content in contents:
            print(content)

    def chd(self, path):
        # Изменить рабочую директорию
        try:
            os.chdir(path)
            print(f"Текущая директория изменена на '{os.getcwd()}'.")
        except FileNotFoundError:
            print(f"Директория не найдена в '{path}'.")

    def cf(self, name, content=""):
        # Создать файл в текущей директории
        with open(name, 'w') as file:
            file.write(content)
        print(f"Файл '{name}' создан.")

    def rf(self, name):
        # Прочитать файл в текущей директории
        try:
            with open(name, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Файл '{name}' не найден в директории.")

    def wf(self, name, content):
        # Записать в файл в текущей директории текст.
        with open(name, 'a') as file:
            file.write(content)
        print(f"Запись в файл '{name}' прошла успешно.")

    def df(self, name):
        # Удалить файл из текущей директории
        try:
            os.remove(name)
            print(f"Файл '{name}' удалён.")
        except FileNotFoundError:
            print(f"Файл '{name}' не найден в директории.")

    def cof(self, src, dest):
        #Копировать файл из одной директории в другую
        try:
            shutil.copy(src, dest)
            print(f"Файл '{src}' скопирован в '{dest}'.")
        except FileNotFoundError:
            print(f"Файл '{src}' не найден в директории.")

    def mf(self, src, dest):
        # Переместить файл из одной директории в другую
        # Указывается путь к файлу, а затем директория для перемещения
        try:
            shutil.move(src, dest)
            print(f"Файл '{src}' перемещён в '{dest}'.")
        except FileNotFoundError:
            print(f"Файл '{src}' не найден в директории.")

    def ref(self, old_name, new_name):
        # Переименовать файл
        try:
            os.rename(old_name, new_name)
            print(f"Файл '{old_name}' переименован в '{new_name}'.")
        except FileNotFoundError:
            print(f"Файл '{old_name}' не найден в директории.")


file_manager = FileManager()

while True:
    command = input("Ввести команду (Введите help, чтобы узнать список команд): ").strip().split()

    if command[0] == 'help':
        print("Список команд:")
        print("  cd <name>: Создать директорию.")
        print("  dd <name>: Удалить директорию.")
        print("  lc: Список файлов в директории.")
        print("  chd <path>: Изменить текущую директорию.")
        print("  cf <name>: Создать файл.")
        print("  rf <name>: Считать файл.")
        print("  wf <name>: Записать в файл.")
        print("  df <name>: Удалить файл.")
        print("  cof <src> <dest>: Копировать файл.")
        print("  mf <src> <dest>: Переместить файл.")
        print("  ref <old_name> <new_name>: Переименовать файл.")
        print("  exit: Закрыть менеджер.")

    elif command[0] == 'cd':
        file_manager.cd(command[1])

    elif command[0] == 'dd':
        file_manager.dd(command[1])

    elif command[0] == 'lc':
        file_manager.lc()

    elif command[0] == 'chd':
        file_manager.chd(command[1])

    elif command[0] == 'cf':
        file_manager.cf(command[1])

    elif command[0] == 'rf':
        file_manager.rf(command[1])

    elif command[0] == 'wf':
        name = command[1]
        content = input("Введите текст для записи: ")
        file_manager.wf(name, content)

    elif command[0] == 'df':
        file_manager.df(command[1])

    elif command[0] == 'cof':
        file_manager.cof(command[1], command[2])

    elif command[0] == 'mf':
        file_manager.mf(command[1], command[2])

    elif command[0] == 'ref':
        file_manager.ref(command[1], command[2])

    elif command[0] == 'exit':
        break

    else:
        print("Не является внутренней или внешней командой, исполняемой программой или пакетным файлом.")
