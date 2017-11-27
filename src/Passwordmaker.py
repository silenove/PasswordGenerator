#!/usr/bin/python
#coding:utf-8
import random
import os,sys
import KeyBoardPwd
import DatePwd
import PYMaker
import WdMaker
import time

class Passwordmaker(object):

    def __init__(self):
        self.date = DatePwd.date_pwd()
        self.word = WdMaker.WdMaker()
        self.pinyin = PYMaker.PYMaker()
        self.keyboard=KeyBoardPwd.KeyBoardPwd()

    #基础返回函数

    #返回数字(键盘模式中)
    def returnNum(self):
        pwd = self.keyboard.get(1)
        return pwd
    #返回单词
    def returnWord(self):
        pwd=self.word.get()
        return pwd
    #返回符号
    def returnSym(self):
        i=random.randint(0,9)
        if i==0:
            return '!'
        elif i==1:
            return '#'
        elif i==2:
            return '$'
        elif i==3:
            return '%'
        elif i==4:
            return '&'
        elif i==5:
            return '*'
        elif i==6:
            return '('
        elif i==7:
            return ')'
        elif i==8:
            return '_'
        elif i==9:
            return '+'
    #返回拼音
    def returnPinYin(self):
        pwd = self.pinyin.get()
        return pwd
    # 返回日期
    def returnDate(self):
        pwd = self.date.mk_date_pwd()
        return pwd
    #返回键盘模式
    def returnKeyBoard(self):
        pwd=self.keyboard.get()
        return pwd

    #混合返回函数
    #返回数字或日期
    def returnNumOrDate(self):
        i = random.randint(0, 1)
        if i == 0:
            return self.returnNum()
        elif i == 1:
            return self.returnDate()

    #返回单词或拼音
    def returnWordOrPinyin(self):
        i = random.randint(0, 1)
        if i == 0:
            return self.returnWord()
        elif i == 1:
            return self.returnPinYin()

    #返回单词或拼音（重叠）
    def returnWorPYoverlap(self):
        i = random.randint(0, 1)
        times = random.randint(2, 5)
        if i == 0:
            return self.returnWord() * times
        elif i == 1:
            return self.returnPinYin() * times

    #返回字母+数字或数字+字母
    def returnCharAndNum(self):
        i = random.randint(0, 1)
        if i==0:
            return self.returnWordOrPinyin()+self.returnNumOrDate()
        elif i==1:
            return self.returnNumOrDate()+self.returnWordOrPinyin()

    #返回字母+键盘模式or键盘模式+字母
    def returnCharAndKB(self):
        i = random.randint(0, 1)
        if i == 0:
            return self.returnWordOrPinyin() + self.returnKeyBoard()
        elif i == 1:
            return self.returnKeyBoard() + self.returnWordOrPinyin()


    #返回字母+符号或符号+字母
    def returnCharAndSym(self):
        i = random.randint(0, 1)
        if i == 0:
            return self.returnWordOrPinyin() + self.returnSym()
        elif i == 1:
            return self.returnSym() + self.returnWordOrPinyin()

    #返回数字+符号或符号+数字
    def returnNumAndSym(self):
        i = random.randint(0, 1)
        if i == 0:
            return self.returnNumOrDate() + self.returnSym()
        elif i == 1:
            return self.returnSym() + self.returnNumOrDate()


    #返回字母+数字+符号(全排列)
    def returnCharAndSymAndNum(self):
        i = random.randint(0, 5)
        if i==0:
            return self.returnWordOrPinyin()+self.returnNumOrDate()+self.returnSym()
        elif i==1:
            return self.returnWordOrPinyin()+self.returnSym()+self.returnNumOrDate()
        elif i==2:
            return self.returnNumOrDate() + self.returnWordOrPinyin()+self.returnSym()
        elif i==3:
            return self.returnNumOrDate()+ self.returnSym()+self.returnWordOrPinyin()
        elif i==4:
            return self.returnSym()+self.returnWordOrPinyin()+self.returnNumOrDate()
        elif i==5:
            return self.returnSym() + self.returnNumOrDate()+self.returnWordOrPinyin()

    #结果生成
    def generate_result(self, intKB, intW_K, intW_N, intW_OL, intN_S, intW_N_S, intLength, intAmount):
        list_choice = []
        result = []
        total = intAmount
        try:
            fname = 'password' + time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time())) + '.txt'
            fhandle = open(os.path.join('result', fname), 'w')
        except:
            return 'not found folder "result/"'
        if intKB == 1:
            list_choice.append('KB')
        if intW_K == 1:
            list_choice.append('W_K')
        if intW_N == 1:
            list_choice.append('W_N')
        if intW_OL == 1:
            list_choice.append('W_OL')
        if intN_S == 1:
            list_choice.append('N_S')
        if intW_N_S == 1:
            list_choice.append('W_N_S')

        step = 0

        while True:
            choice = random.choice(list_choice)
            step += 1
            if choice == 'KB':
                passwd = self.returnKeyBoard()
            elif choice == 'W_K':
                passwd = self.returnCharAndKB()
            elif choice == 'W_N':
                passwd = self.returnCharAndNum()
            elif choice == 'W_OL':
                passwd = self.returnWorPYoverlap()
            elif choice == 'N_S':
                passwd = self.returnNumAndSym()
            elif choice == 'W_N_S':
                passwd = self.returnCharAndSymAndNum()

            if len(passwd) > 5 and len(passwd) <= intLength and passwd not in result:
                fhandle.write(passwd+'\n')
                intAmount -= 1
                result.append(passwd)

            if intAmount <= 0:
                break

            if step >= 1000000:
                break
        
        fhandle.close()

        if step >= 1000000 and intAmount > 0:
            return 'time limited. generate ' + str(total - intAmount) + ' passwords.\n file : ' + fname + '.'
        else:
            return 'finished. generate file ' + fname + '.' 
            

