readtxt = """
this is a wonderful day!
can you call me name?
my name is Zhujunjie.
"""

def word(readtxt):
    readlist = readtxt.split()
    dict={}
    for every_word in readlist:
        if every_word in dict:
            dict[every_word]+=1
        else:
            dict[every_word]=1
    return dict

def test(test1,test2):
    return_li=[]
    word_list1=test1.splitlines()
    word_list2=test2.splitlines()
    li_word1=[column for column in word_list1 if column and column.isspace()]
    li_word2=[column for column in word_list2 if column and column.isspace()]
    li_len1=len(li_word1)
    li_len2=len(li_word2)
    for step in range(max(li_len1,li_len2)):
        if step<li_len1 and step<li_len2:
            li_coll1=li_word1[step].split()
            li_coll2=li_word2[step].split()
            if li_coll1 != li_coll2:
                return_li.append((word_list1.index(li_word1[step]),
                                  word_list2.index(li_word2[step]),
                                  li_word1[step],li_word2[step]))
            else:
                if li_len1>li_len2:
                    return_li.append((word_list1.index(li_word1[step]), -1,li_word1[step],''))
                else:
                    return_li.append((-1,word_list2.index(li_word2[step]), '',li_word2[step]))
        return return_li