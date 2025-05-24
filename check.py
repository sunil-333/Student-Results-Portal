import re


def checkRoll(roll):
    if len(roll) != 10:
        return False
    reg = re.compile('[0-9a-zA-z]{10}')
    return reg.match(roll) != None


def checkFile(fileName):
    return '.' in fileName and fileName.rsplit('.', 1)[-1] == 'csv'
