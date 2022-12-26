import pickle
import json
import os

workSpace = ''
defaultForm = 'default'

def wordForm(word:str, wordForm:str):
    global workSpace, defaultForm
    word = word + '.txt'
    if (word in os.listdir(workSpace)):
        f = open(workSpace + '\\' + word, 'r')
        ff = json.loads(f.read())
        if (wordForm in ff) and ((ff[wordForm] != '') and (ff[wordForm] != ' ')):
            return ff[wordForm]
        elif (ff[defaultForm] != '' and ff[defaultForm] != ' ') : 
            return ff[defaultForm]
        else:
            return word.replace('.txt',''), '(No forms in file)'
    else:
        return word.replace('.txt',''), '(No word file)'

def setWorkSpace(folderName:str):
    global workSpace
    workSpace = folderName + r'\wordList'

def setDefaultForm(formName:str):
    global defaultForm
    defaultForm = formName
    

def createDefaultForm(folderName:str, numOfForms:int):
    global defaultForm
    f = open(folderName + '\wordList\defaultForm.txt', 'w')
    res = {}
    for i in range(numOfForms):
        if i == 0:
            res[defaultForm] = '-input your word here-'
        else:
            res[str(i + 1)] = ''
    f.write(json.dumps(res))
    f.close


def createWorkSpace(folderName:str): 
    global workSpace
    if (folderName not in os.listdir()):
        os.mkdir(folderName)
        os.mkdir(folderName + '\wordList')
    else: 
        print('This folder already exists')
    createDefaultForm(folderName, 1)
    workSpace = folderName + '\wordList'
