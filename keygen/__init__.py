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
