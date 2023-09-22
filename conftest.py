from checks import checkout
import pytest
import yaml
from _datetime import datetime
from os import path

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    print({data['folderin']})
    print({data['folderout']})
    return checkout(f"mkdir -p {data['folderin']} {data['folderout']} {data['folderext']}", '')


@pytest.fixture()
def make_files():
    return checkout(f"cd {data['folderin']}; touch file1 file2", '')


# Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига,
# статистика загрузки процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла).

@pytest.fixture()
def logger():

    # Выполняется перед каждым шагом теста
    now = datetime.now().strftime("[%Y-%m-%d] %H:%M:%S")
    number_of_files = len(data)
    size = path.getsize('config.yaml')
    with open('stat.txt', 'w') as stat:
        stat.write(f"{now} - |Number of files:{number_of_files}| Size:{size} bytes|\n")
        with open(data['statisticpath'], 'r') as bot:
            for line in bot:
                stat.write(line)
    yield

    # Выполняется после каждого шага теста
    now = datetime.now().strftime("[%Y-%m-%d] %H:%M:%S")
    number_of_files = len(data)
    size = path.getsize('config.yaml')
    with open('stat.txt', 'a') as stat:
        stat.write(f"{now} - |Number of files:{number_of_files}| Size:{size} bytes|\n")
        with open('D:\Educational materials\GeekBrains\Python\loadavg.txt', 'r') as bot:
            for line in bot:
                stat.write(line)

