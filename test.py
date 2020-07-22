import sys
import codecs
from Tree import BinarySearchTree
T = BinarySearchTree()
first = 0
second = 0
first = 1920
second = 2019
l =[[ "аниме",[]],["фэнтези",[]],["мелодрама",[]],["биография",[]],["боевик",[]],["вестерн",[]],["военный",[]],["детектив",[]],["документальный",[]],["драма",[]],
            ["мультфильм",[]],["приключения",[]],["семейный",[]], ["триллер",[]], ["ужасы",[]], ["фантастика",[]]]
dic = {}
file = codecs.open('C:\\Users\\alexa\\Documents\\Films.txt', 'r', 'utf_8_sig' )
for line in file:
    A = line.split(', ')
    for j in range(len(l)):
        if(A[2]==l[j][0]):
            l[j][1].append(A)
diclist = []
for k in range(first,second+1):
    diclist.append(k)
dic =dict.fromkeys(diclist[:])
for k in range(first,second+1):
    d = []
    for j in range(len(l)):
        if(l[j][1]!=[]):
            for q in range((len(l[j][1]))):
                if(int(l[j][1][q][1])==k):
                    d.append((l[j][1][q]))
    dic.update({int(k):d})
print(dic)
    

