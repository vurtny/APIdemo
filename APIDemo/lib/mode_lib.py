import hashlib


def set_pwd(password):
    pwd = hashlib.md5()
    # pwd.update(password.encode('utf-8'))
    password = pwd.hexdigest()
    print("加密后：", password)
    return password


