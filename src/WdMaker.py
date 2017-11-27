
import random
import math


class WdMaker(object):
    def __init__(self):
        try:
            fhandle1 = open('seed/yahoo_word_top50.txt', 'r')
            fhandle2 = open('seed/csdn_word_top50.txt', 'r')
        except IOError as e:
            raise('IOError', e)
        #lines = fhandle.readlines()
        self.dict_word = {}
        self.length = 0
        for line in fhandle1:
            line = line[:-1]
            items = line.split(':')
            num = int(math.sqrt(int(items[1])))
            self.length += num
            self.dict_word[items[0]] = self.length

        for line in fhandle2:
            line = line[:-1]
            items = line.split(':')
            num = int(math.sqrt(int(items[1])))
            self.length += num
            if items[0] in self.dict_word.keys():
                self.length -= num
            else:
                self.dict_word[items[0]] = self.length

        fhandle1.close()
        fhandle2.close()

        self.items_word = sorted(self.dict_word.items(), key=lambda x: x[1], reverse=False)
        #self.list_py = list(map(lambda x: x[:-1], lines))
        #self.length = len(self.list_py)

    def get(self):
        seed = random.randint(0, self.length)
        for item in self.items_word:
            word, num = item[0], item[1]
            if seed <= num:
                result = word
                break
#        print(result)
        return result


