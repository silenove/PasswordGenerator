# -*- coding:utf-8 -*-
# author: liangzhizhou
# email : liangzhizhou@iie.ac.cn
import os, sys
import random


class KeyBoardPwd:
    def __init__(self):
        self.keyboard_pwdinfo = self.read_figure_result()

    def read_figure_result(self):
        keyboard_pwdinfo = []
        with open("seed/KeyBoardresult.txt", 'r') as fr:
            for each in fr:
                if each.strip() == '': break
            pwd, num, mode = ['0'], [0], 0
            for each in fr:
                tmp = each.strip().split('\t')
                if tmp[0] != '':
                    pwd.append(tmp[0])
                    num.append(int(tmp[1]))
                    num[-1] = num[-1] + num[-2]
                else:
                    keyboard_pwdinfo.append([])
                    keyboard_pwdinfo[mode].append(pwd)
                    keyboard_pwdinfo[mode].append(num)
                    pwd, num = ['0'], [0]
                    mode = mode + 1
        return keyboard_pwdinfo

    # get pwd based on keyboard mode randomly; type>=0 means that return_value is digit
    def get(self, type=-1):
        if type < 0:
            total_num = 0
            for each_type in self.keyboard_pwdinfo:
                total_num += each_type[1][-1]
            total_num -= self.keyboard_pwdinfo[3][1][-1]
            total_num += self.keyboard_pwdinfo[0][1][-1]

            # choose type from samerow,zigzag,snake,digit
            choose_type = 0
            random_num = random.randint(1, total_num)
            for each_type in self.keyboard_pwdinfo:
                random_num -= each_type[1][-1]
                if random_num <= 0:
                    break
                else:
                    choose_type += 1

        else:
            choose_type = 3
        # choose pwd from choosen type randomly
        choose_pwdinfo = self.keyboard_pwdinfo[choose_type]
        random_num = random.randint(1, choose_pwdinfo[1][-1])
        low, high = 1, len(choose_pwdinfo[1])
        while low < high:
            mid = (low + high) // 2
            if choose_pwdinfo[1][mid] < random_num:
                low = mid + 1
            else:
                high = mid
        return choose_pwdinfo[0][low]


#if __name__ == "__main__":
#    keyboardpwd = KeyBoardPwd()
#    pwd = keyboardpwd.get()
#    print (keyboardpwd.get(1))
#     print (pwd)

