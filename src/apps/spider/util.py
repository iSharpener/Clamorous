import hashlib

def init_md5(str):
    m2 = hashlib.md5()
    m2.update(str.encode('utf8'))
    return m2.hexdigest()
