# AL3X V3GAS KeyGen
# AL3X V3GAS 2016 (C)
# The AVX Project 2016 (C)

import random

def keygen():
    rp1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rp2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    c = -1000000
    d = 1000000
    a = -1000000000
    b = 1000000000
    code1 = random.randint(a,b)
    code2 = random.randint(c,d)
    let1 = random.choice(rp1)
    let2 = random.choice(rp2)
    codef = str(let1) + str(code1) + str(let2) + str(code2)
    return codef

def small():
    rp1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rp2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rp3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
    rp4 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
    let1 = random.choice(rp1)
    let2 = random.choice(rp2)
    let3 = random.choice(rp3)
    let4 = random.choice(rp4)
    code = str(let1) + str(let3) + str(let4) + str(let2)
    return code