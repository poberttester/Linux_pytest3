import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    # print('*'*30)
    # print(f'{result=}')
    # print('*' * 30)
    # print(text)
    # print('*' * 30)
    # print(result.stdout)
    # print('*' * 30)
    # print(result.returncode)
    # print('*' * 30)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if text in result.stdout or text in result.stderr:
        return True
    else:
        return False
