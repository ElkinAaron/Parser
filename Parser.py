#!/usr/bin/env python
# -*- coding: utf-8 -*-
# see http://stackoverflow.com/questions/3170211/why-declare-unicode-by-string-in-python

import unicodedata


def Parser(file):

    Hash = {}
    Hashnumber = 1


    #loops until the parsing is done.
    with open(file) as file:
        for line in file:
            #Turns the unicode into ascii to make it easier to work with
            line = Normalizer(line)
            #Breaks the string up by word
            LineA = line.split()
            #Itemizes the words in the tweets, breaking them up and giving them a counter
            itemlist = Itemize(LineA)
            #Loops through the tweet allowing the parsing of ngrams
            (Hash, Hashnumber) = GramParser(itemlist, Hash, Hashnumber)

#    return Hash
    writer = csv.writer(open('dict.csv', 'wb'))
    for key, value in Hash.items():
        writer.writerow([key, value])





def Normalizer(line):
    return unicodedata.normalize('NFKD', line).encode('ascii','ignore')



def Itemize(LineA):
    itemlist = []
    for item in LineA:
        itemlist.append(item)
    return itemlist




def GramParser(itemlist, Hash, Hashnumber):
    x = 0
    while x < len(itemlist):
        #Adds the trigrams from the tweet into the Hash
        if x+2 < len(itemlist):
            gram = itemlist[x]+" "+itemlist[x+1]+" "+itemlist[x+2]
            Bool1= gram in Hash
            if Bool1 == False:
                Hash[gram] = Hashnumber
                Hashnumber=Hashnumber+1
        #Adds the bigrams from the tweet into the Hash
        if x+1 < len(itemlist):
            gram = itemlist[x]+" "+itemlist[x+1]
            Bool2 = gram in Hash
            if Bool2 == False:
                Hash[gram] = Hashnumber
                Hashnumber=Hashnumber+1
        gram = itemlist[x]
        Bool3 = gram in Hash
        #Adds the unigrams from the tweet into the Hash
        if Bool3 == False:
            Hash[gram] = Hashnumber
            Hashnumber=Hashnumber+1
        x=x+1
    return Hash, Hashnumber




def NormalizeThat():
    String= u"@S_Remilia UFO„Å∞„Åã„ÇäË¶ã„Å¶Â§úÊõ¥„Åã„Åó„Åó„Å™„ÅÑ„Çà„ÅÜ„Å´„Å™„ÄÅS„É¨„Éü„É™„Ç¢"
    return unicodedata.normalize('NFKD', String).encode('ascii','ignore')

def NormalizeThis(String):
    return unicodedata.normalize('NFKD', String).encode('ascii','ignore')



def Itemizetester():
    string = "We are having a fine day"
    string = string.split()
    output = Itemize(string)
    print(output)

    string = "b'@S_Remilia UFOAAaCaEaAAuEoAaAoAoATMANCaAUA ATMAASE EuETMC'"
    string = string.split()
    output = Itemize(string)
    print(output)

    string = "b'Mavrix Photo Inc hiring paparazzi... - #NewYork , NY (http://t.co/6tpXjqqA) Get Photography Jobs #Photography #jobs #job #GetAllJobs'"
    string = string.split()
    output = Itemize(string)
    print(output)

    string = "b'.:. Porque no, primero pajareamos y despus check in! Jajajajaja! Ysk lo logramos! .:. (@ Stanford Hotel) http://t.co/V8ybprwV'"
    string = string.split()
    output = Itemize(string)
    print(output)



def GramParserTester():
    stringlist = ['We', 'are', 'having', 'a', 'fine', 'day']
    Hash = {}
    Hashnumber = 0
    (Hash, Hashnumber) = GramParser(stringlist, Hash, Hashnumber)
    print(Hash)

    stringlist = ['We', 'are', 'going', 'to', 'the', 'movies', 'on', 'this', 'fine', 'day']
    (Hash, Hashnumber) = GramParser(stringlist, Hash, Hashnumber)
    print(Hash)

    stringlist = ["b'@S_Remilia", 'UFOAAaCaEaAAuEoAaAoAoATMANCaAUA', 'ATMAASE', "EuETMC'"]
    Hash = {}
    Hashnumber = 0
    Hash = GramParser(stringlist, Hash, Hashnumber)
    print(Hash)

    stringlist = ["b'Mavrix", 'Photo', 'Inc', 'hiring', 'paparazzi...', '-', '#NewYork', ',', 'NY', '(http://t.co/6tpXjqqA)', 'Get', 'Photography', 'Jobs', '#Photography', '#jobs', '#job', "#GetAllJobs'"]
    Hash = {}
    Hashnumber = 0
    Hash = GramParser(stringlist, Hash, Hashnumber)
    print(Hash)

    stringlist = ["b'.:.", 'Porque', 'no,', 'primero', 'pajareamos', 'y', 'despus', 'check', 'in!', 'Jajajajaja!', 'Ysk', 'lo', 'logramos!', '.:.', '(@', 'Stanford', 'Hotel)', "http://t.co/V8ybprwV'"]
    Hash = {}
    Hashnumber = 0
    Hash = GramParser(stringlist, Hash, Hashnumber)
    print(Hash)

    stringlist = ['We', 'are', 'having', 'a', 'fine', 'day']
    Hash = {}
    Hashnumber = 0
    Hash = GramParser(stringlist, Hash, Hashnumber)
#    print(Hash)

    stringlist = ["b'@S_Remilia", 'UFOAAaCaEaAAuEoAaAoAoATMANCaAUA', 'ATMAASE', "EuETMC'"]
    Hash = GramParser(stringlist, Hash, Hashnumber)
#    print(Hash)

    stringlist = ["b'Mavrix", 'Photo', 'Inc', 'hiring', 'paparazzi...', '-', '#NewYork', ',', 'NY', '(http://t.co/6tpXjqqA)', 'Get', 'Photography', 'Jobs', '#Photography', '#jobs', '#job', "#GetAllJobs'"]
    Hash = GramParser(stringlist, Hash, Hashnumber)
#    print(Hash)

    stringlist = ["b'.:.", 'Porque', 'no,', 'primero', 'pajareamos', 'y', 'despus', 'check', 'in!', 'Jajajajaja!', 'Ysk', 'lo', 'logramos!', '.:.', '(@', 'Stanford', 'Hotel)', "http://t.co/V8ybprwV'"]
    Hash = GramParser(stringlist, Hash, Hashnumber)
    print(Hash)
