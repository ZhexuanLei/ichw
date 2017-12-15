
# coding: utf-8

# In[1]:


"""wcount.py: count words from an Internet file.

__author__ = "Leizhexuan"
__pkuid__  = "1700011714"
__email__  = "lzx1700011714@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    def getwords(lines):
        subparts = lines.lower().split()
        dic = []
        for string in subparts:
            subsubpart = list(string)
            word = ''
            for chrt in subsubpart:
                if chrt.isalpha():
                    word += chrt
            dic += [word] 
        return(dic)
    def count_one(word):
        freq = 0
        for i in dic:
            if i == word:
                freq = freq + 1
        return(freq)
    dic = getwords(lines)
    freq_list = []
    counted_lst = []
    for k in dic:
        if k not in counted_lst:
            freq_list.append(count_one(k))
            counted_lst += [k]        
    freq_list.sort()
    top_freq_list = freq_list[-int(topn):]
    top_freq_list = list(set(top_freq_list))
    top_freq_list.sort()
    top_freq_list.reverse()
    for i in top_freq_list:
        for k in counted_lst:
            if count_one(k) == i:
                print(k + " "*(12-len(k)) + str(i))
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)

