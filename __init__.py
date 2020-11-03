#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: __init__.py
# Author: cluckbird
# Mail: admin@muzmn.cn
# Created Time:  2020-11-3 16:35
#############################################

import hashlib
 
def sha512(data: str):
    hash512 = hashlib.sha512()
    hash512.update(data.encode('utf-8'))
    return hash512.hexdigest()
def sha256(data: str):
    hash256 = hashlib.sha256()
    hash256.update(data.encode('utf-8'))
    return hash256.hexdigest()
def sha1(data: str):
    hash1 = hashlib.sha1()
    hash1.update(data.encode('utf-8'))
    return hash1.hexdigest()
