#!/usr/bin/env python3

import sys

msgbox1 = ["Hi,","Wao,","Hey,","Lucky!","HoyHoy!","This You!","Ah...,","HaHaHa!!","Like you,","Nice to meet you!"]

try:
    mynumber = int(input("Input Your Favorite Number(1~20):"))
except ValueError:
    print("Input Number!!(1~20)")
else:
    if mynumber < 10:
        print(msgbox1[mynumber] + " I Love You!!")
    elif mynumber < 20:
        print(msgbox1[mynumber-10] + "I Hate You...!!")
    else:
        print("Did you have significan other when you were 20???")

