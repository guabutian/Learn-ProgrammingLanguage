#!/usr/bin/python
# -*- coding: cp936 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print s.recv(1024)
s.close()
