# !/usr/bin/python
# coding: utf-8
# Author: BaiyangLi

import random
from datetime import datetime, timedelta


class date_pwd:
    def __init__(self):
        self.begin = [1960, 1, 1]  # date range in [1900.1.1-2099.12.31]
        self.end = [2018, 12, 31]
        self.bounds = self.read_figure_file()  # the number ranges of pwds matched date format
        self.sum = self.bounds[-1]
        self.date = ''

    # read the configure file and get the number of each date format
    def read_figure_file(self):
        nums = []
        bounds = []
        with open("seed/date_num", "rU") as config_file:
            config_line = config_file.readline().strip('\n')
            while (config_line):
                nums += (config_line.split(':')[1].split(','))
                config_line = config_file.readline().strip('\n')

            nums = map(int, nums)
            for count in nums:
                if len(bounds) > 0:
                    bounds.append(count + bounds[len(bounds) - 1])
                else:
                    bounds.append(count)
            return bounds

    # according to the frequency of each date format, make date_format pwd
    def mk_date_pwd(self):
        t1 = datetime(self.begin[0], self.begin[1], self.begin[2])
        t2 = datetime(self.end[0], self.end[1], self.end[2])

        t = random.randint(1, (t2 - t1).days)
        date_tuple = t1 + timedelta(t)

        case = random.randint(1, self.sum)
        tmp = ''

        if case <= self.bounds[0]:
            tmp = datetime.strftime(date_tuple, "%Y%m%d")
            self.date = tmp[2:]
        elif case > self.bounds[0] and case <= self.bounds[1]:
            tmp = datetime.strftime(date_tuple, "%m%d%Y")
            self.date = tmp[:4] + tmp[6:]
        elif case > self.bounds[1] and case <= self.bounds[2]:
            tmp = datetime.strftime(date_tuple, "%d%m%Y")
            self.date = tmp[:4] + tmp[6:]

        elif case > self.bounds[2] and case <= self.bounds[3]:
            self.date = datetime.strftime(date_tuple, "%Y%m%d")
        elif case > self.bounds[3] and case <= self.bounds[4]:
            self.date = datetime.strftime(date_tuple, "%m%d%Y")
        else:
            self.date = datetime.strftime(date_tuple, "%d%m%Y")
        # print self.date
        return self.date

# a=date_pwd()
# for i in range(20):
#	a.mk_date_pwd()

