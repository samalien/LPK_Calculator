#---------------------------------------------
def calcul_carre(x):
    return "Fonction manquante !"

def calcul_cube(x):
    return "Fonction manquante !"

def calcul_factoriel(x):
    return "Fonction manquante !"

def calcul_pgcd(x, y):
    return "Fonction manquante !"


def calcul_ppcm(a, b):
    return "Fonction manquante !"


def decompose(n):
    return "Fonction manquante !"


def calcul_premier(x):
    return "Fonction manquante !"

def calcul_parfait(x):
    return "Fonction manquante !"

def calcul_tg(x):
    return "Fonction manquante !"

def calcul_sin(x):
    return "Fonction manquante !"

def calcul_cos(x):
    return "Fonction manquante !"

def dec_bin(x):
    return "Fonction manquante !"


def bin_dec(x):
    return "Fonction manquante !"


def dec_oct(x):
    return "Fonction manquante !"


def oct_dec(x):
    return "Fonction manquante !"


def dec_hex(x):
    return "Fonction manquante !"


def hex_dec(x):
    return "Fonction manquante !"


def hex_bin(x):
    return "Fonction manquante !"


def oct_bin(x):
    return "Fonction manquante !"


def bin_hex(x):
    return "Fonction manquante !"


def bin_oct(x):
    return "Fonction manquante !"


def hex_oct(x):
    return "Fonction manquante !"


def oct_hex(x):
    return "Fonction manquante !"


#-----------------------------------------
def calcul_carre(x):
    return x*x

def calcul_cube(x):
    return x**3
def calcul_factoriel(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

def calcul_parfait(x):
    s=0
    for i in range(1,x):
        if x%i==0:
            s=s+i
    return s==x

def calcul_pgcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def calcul_ppcm(a, b):
    """ppcm(a,b): calcul du 'Plus Petit Commun Multiple' entre 2 nombres entiers a et b"""
    if (a == 0) or (b == 0):
        return 0
    else:
        return (a * b) // calcul_pgcd(a, b)


def decompose(n):
    print("%d=1" % (n), end=' ')
    i = 2
    res = ""
    while n > 1:
        while n % i == 0:
            res = res + str(i) + ' *'
            n = n / i
        i = i + 1
    return res[:-1]


def calcul_premier(x):
    nb = 0
    for i in range(1, x + 1):
        if x % i == 0:
            nb = nb + 1
    return nb == 2


def dec_bin(x):
    r = ''
    while x != 0:
        r = str(x % 2) + r
        x = int(x / 2)
    return r


def bin_dec(x):
    y = str(x)
    exp = len(y) - 1
    s = 0
    for i in y:
        s = s + int(i) * pow(2, exp)
        exp -= 1
    return s


def dec_oct(x):
    r = ''
    while x != 0:
        r = str(x % 8) + r
        x = int(x / 8)
    return r


def oct_dec(x):
    y = str(x)
    exp = len(y) - 1
    s = 0
    for i in y:
        s = s + int(i) * pow(8, exp)
        exp -= 1
    return s


def dec_hex(x):
    r = ''
    while x != 0:
        list = ['A', 'B', 'C', 'D', 'E', 'F']
        if x % 16 >= 10:
            c = list[(x % 16) - 10]
        else:
            c = str(x % 16)
        r = c + r
        x = int(x / 16)
    return r


def hex_dec(x):
    # s=int(x, 16)
    y = str(x)
    exp = len(y) - 1
    s = 0
    for i in y:
        if i in ['A', 'B', 'C', 'D', 'E', 'F']:
            i = ord(i) - 65 + 10
        s = s + int(i) * pow(16, exp)
        exp -= 1
    return s


def hex_bin(x):
    x = hex_dec(x)
    x = dec_bin(x)
    return x


def oct_bin(x):
    x = oct_dec(x)
    x = dec_bin(x)
    return x


def bin_hex(x):
    x = bin_dec(x)
    x = dec_hex(x)
    return x


def bin_oct(x):
    x = bin_dec(x)
    x = dec_oct(x)
    return x


def hex_oct(x):
    x = hex_dec(x)
    x = dec_oct(x)
    return x


def oct_hex(x):
    x = oct_dec(x)
    x = dec_hex(x)
    return x
