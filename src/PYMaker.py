#coding=utf-8
#! /usr/bin/env python
#################################################################################
#     File Name           :     PYMaker.py
#     Created By          :     silenzhou
#     Creation Date       :     [2017-11-2 21:39]
#     Last Modified       :     [2017-11-27 17:02]
#     Description         :      
#################################################################################
#/*************************************************************************
#
#	> File Name: PYMaker.py
#	> Author: 
#	> Mail: 
#	> Created Time: 四 11/2 21:39:07 2017
# ************************************************************************/

import random
import math


class PYMaker(object):
    def __init__(self):
        try:
            fhandle = open('seed/pinyin_top200.txt', 'r')
        except IOError as e:
            raise('IOError', e)
        #lines = fhandle.readlines()
        self.dict_py = {}
        self.length = 0
        for line in fhandle:
            line = line[:-1]
            items = line.split(':')
            num = int(math.sqrt(int(items[1])))
            self.length += num
            self.dict_py[items[0]] = self.length
        self.items_py = sorted(self.dict_py.items(), key=lambda x: x[1], reverse=False)
        #self.list_py = list(map(lambda x: x[:-1], lines))
        #self.length = len(self.list_py)

    def get(self):
        seed = random.randint(0, self.length)
        for item in self.items_py:
            py, num = item[0], item[1]
            if seed <= num:
                result = py
                break
        return result

        
