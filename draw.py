# encoding=utf-8

import random
import os

strMenu = """——————随机点名器——————
1.批量点名
2.不重复点名
3.重复点名
4.编辑名单
5.退出
——————你值得信赖——————"""
listName = []

def start():
    while True:
        print(strMenu)
        x = int(input(":"))
        
        if x == 1:
            os.system("cls")
            batchRoll()
            os.system("cls")
            continue
        elif x == 2:
            os.system("cls")
            noRepeatRoll()
            os.system("cls")
            continue
        elif x == 3:
            os.system("cls")
            RepeatRoll()
            os.system("cls")
            continue
        elif x == 4:
            os.system("cls")
            editList()
            os.system("cls")
            continue
        else:
            break

def batchRoll():
    if os.path.exists(r".\list.txt"):
        fo = open("list.txt","r")
    else:
        open("list.txt","w")
        return
    
    listName = fo.read().splitlines()
    counting = int(input("点名次数："))

    for i in range(counting):
        if listName:
            name = random.choice(listName)
            print(name)
            listName.remove(name)
    
    input(":")
    fo.close()
    listName = []

def noRepeatRoll():
    if os.path.exists(r".\list.txt"):
        fo = open("list.txt","r")
    else:
        open("list.txt","w")
        return
    listName = fo.read().splitlines()
    
    while True:
        if listName:
            name = random.choice(listName)
            print(name)
            listName.remove(name)

            #连续点名
            x = input(":")
            if x == '0':
                break
            else:
                continue
        else:
            break

    fo.close()
    listName = []

def RepeatRoll():
    if os.path.exists(r".\list.txt"):
        fo = open("list.txt","r")
    else:
        open("list.txt","w")
        return
    listName = fo.read().splitlines()
    
    if listName:
        while True:
                name = random.choice(listName)
                print(name)

                #连续点名
                x = input(":")
                if x == '0':
                    break
                else:
                    continue

    fo.close()
    listName = []

def editList():
    os.startfile("list.txt")

start()