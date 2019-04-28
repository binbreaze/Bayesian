# -*- coding: UTF-8 -*-
import re

def text2wordlist(bigtext):   #处理文本，转换成words列表
    text_split = re.split(r'/W*',bigtext)
    return [words.lower() for words in text_split if len(words)>2]

def create2setlist(wordlist):  #将所有的word组成一个大字典
    wordset = set()
    print(type(wordset))
    for dec in wordlist:
        wordset = wordset | set(dec)
    return wordset

def setOfwords2vec(wordset,inputset):   # 创建词向量
    setofwords = [0] * len(wordset)
    for word in inputset:
        if word in wordset:
            setofwords[wordset.index(word)] = 1
        else:
            print("the words is not in mydict!!!")
        return setofwords
def bagOfwords2vec(wordset,inputset):    #创建词袋模型
    setof_bagwords = [0] * len(wordset)
    for word in inputset:
        if word in wordset:
            setof_bagwords[wordset.index(word)] += 1
        else:
            print("the word is not in mydict!!!")
        return setof_bagwords





