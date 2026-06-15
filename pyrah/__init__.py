#!/bin/env python3

import ctypes
import numpy as np

LIBNAME = "librah.so"
CLIB = "libc.so.6"

libname = LIBNAME
__rah = ctypes.CDLL(libname)
__c = ctypes.CDLL(CLIB)

def get_max_buffer_size():
    return __rah.rah_max_buffer_size()

def rah_write(appid, d_buf):
    if type(d_buf) != bytes:
        raise Exception("Data buffer should be type of bytes")

    buffer = ctypes.create_string_buffer(len(d_buf))
    __c.memcpy(buffer, d_buf, len(d_buf))
    __rah.rah_write.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_ulong]

    __rah.rah_write(appid, buffer, len(d_buf))

def rah_read(appid, d_len):
    ptr = ctypes.create_string_buffer(d_len)
    __rah.rah_read.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_ulong]

    __rah.rah_read(appid, ptr, d_len)
    return ptr.raw

def rah_clear_buffer(appid):
    __rah.rah_clear_buffer.argtypes = [ctypes.c_int]
    __rah.rah_clear_buffer(appid)
