#!/bin/env python3

import ctypes
import numpy as np

LIBNAME = "librah.so"
CLIB = "libc.so.6"

libname = LIBNAME
__rah = ctypes.CDLL(libname)
__c = ctypes.CDLL(CLIB)

def __get_buffer(appid, size):
    __rah.rah_request_mem.restype = ctypes.c_ulong
    buffer = __rah.rah_request_mem(appid, size)
    return buffer

def __remove_buffer(buffer):
    return __rah.rah_free_mem(buffer)

def __write_buffer(appid, buffer, d_len):
    __rah.rah_write_mem.argtypes = [ctypes.c_ubyte, ctypes.c_char_p, ctypes.c_ulong]
    __rah.rah_write_mem(appid, buffer, d_len)

def get_max_buffer_size():
    return __rah.rah_max_buffer_size()

def rah_write(appid, d_buf):
    MAX_DATA_SIZE = get_max_buffer_size()
    if type(d_buf) != bytes:
        raise Exception("Data buffer should be type of bytes")

    for i in range(0, len(d_buf), MAX_DATA_SIZE):
        sending_len = MAX_DATA_SIZE if i + MAX_DATA_SIZE < len(d_buf) else len(d_buf) - i
        buffer = __get_buffer(appid, sending_len)
        buf_loc = ctypes.c_char_p(buffer)
        data = np.array(d_buf[i:i+sending_len]).ctypes.data_as(ctypes.c_char_p)
        __c.memcpy(buf_loc, data, sending_len)
        __write_buffer(appid, buf_loc, sending_len)
        __remove_buffer(buf_loc)

def rah_read(appid, d_len):
    ptr = ctypes.create_string_buffer(d_len)
    __rah.rah_read.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_ulong]

    __rah.rah_read(appid, ptr, d_len)
    return ptr.raw

def rah_clear_buffer(appid):
    __rah.rah_clear_buffer.argtypes = [ctypes.c_int]
    __rah.rah_clear_buffer(appid)
