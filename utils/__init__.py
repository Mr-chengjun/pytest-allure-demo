import hashlib


def md5_hex(strs):
    return hashlib.md5(strs.encode(encoding='UTF-8')).hexdigest()
