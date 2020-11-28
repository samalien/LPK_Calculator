from PyQt5 import QtCore, QtGui, QtWidgets
from fenetre import Ui_LPK_Calculator
import math
import sys
from fonctions import *
check = None
base = 10
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_LPK_Calculator()
ui.setupUi(MainWindow)
MainWindow.show()



# -----------------------------------------------------------#
#                       Les chiffres                         #
# -----------------------------------------------------------#
ui.b_dec.setStyleSheet("background-color: rgb(255,85,127)")

#-------------------------------0----------------------------#
def zero():
    global check
    global base
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "0")
    if not check:
        ui.lineEdit.setText("0")
    check = True
    base = 10
    check_base()

#-------------------------------1----------------------------#
def un():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "1")
    if not check:
        ui.lineEdit.setText("1")
    check = True

#-------------------------------2----------------------------#
def deux():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "2")
    if not check:
        ui.lineEdit.setText("2")
    check = True

#-------------------------------3----------------------------#
def trois():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "3")
    if not check:
        ui.lineEdit.setText("3")
    check = True

#-------------------------------4----------------------------#
def quatre():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "4")
    if not check:
        ui.lineEdit.setText("4")
    check = True

#-------------------------------5----------------------------#
def cinq():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "5")
    if not check:
        ui.lineEdit.setText("5")
    check = True

#-------------------------------6----------------------------#
def six():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "6")
    if not check:
        ui.lineEdit.setText("6")
    check = True

#-------------------------------7----------------------------#
def sept():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "7")
    if not check:
        ui.lineEdit.setText("7")
    check = True

#-------------------------------8----------------------------#
def huit():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "8")
    if not check:
        ui.lineEdit.setText("8")
    check = True

#-------------------------------9----------------------------#
def neuf():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "9")
    if not check:
        ui.lineEdit.setText("9")
    check = True


# -----------------------------------------------------------#
#                      Les parentheses                       #
# -----------------------------------------------------------#
def ouvrante():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "(")
    if not check:
        ui.lineEdit.setText("(")
    check = True


def fermante():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + ")")
    if not check:
        ui.lineEdit.setText(")")
    check = True


# -----------------------------------------------------------#
#                       Les operateurs                       #
# -----------------------------------------------------------#
def virgule():
    global check
    global base
    base = 10
    check_base()
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + ",")
    if not check:
        ui.lineEdit.setText(",")
    check = True


def point():
    global base
    base = 10
    check_base()
    ui.lineEdit.setText(ui.lineEdit.text() + ".")

def plus():
    global base
    base = 10
    check_base()
    ui.lineEdit.setText(ui.lineEdit.text() + "+")


def moins():
    global base
    base = 10
    check_base()
    ui.lineEdit.setText(ui.lineEdit.text() + "-")


def fois():
    global base
    base = 10
    check_base()
    ui.lineEdit.setText(ui.lineEdit.text() + "*")


def sur():
    global base
    base = 10
    check_base()
    ui.lineEdit.setText(ui.lineEdit.text() + "/")


def delete():
    global base
    base = 10
    check_base()
    ui.lineEdit.setText(ui.lineEdit.text()[0:-1])


# -----------------------------------------------------------#
#                 Utilitaires                               #
# -----------------------------------------------------------#
def clear():
    global base
    base = 10
    check_base()
    ui.lineEdit.setText("")


def egal():
    global check
    global base
    base = 10
    check_base()
    if str(ui.lineEdit.text()).find("PGCD") != -1:
        try:
            r = str(ui.lineEdit.text()).split(",")
            n1 = (r[0][5:])
            n2 = (r[1][:-1])
            if n1.isnumeric() and n2.isnumeric():
                n1 = int(r[0][5:])
                n2 = int(r[1][:-1])
                ui.lineEdit.setText(str(calcul_pgcd(n1, n2)))
            else:
                ui.lineEdit.setText("error PGCD")
        except:
            ui.lineEdit.setText("error PGCD")
    elif str(ui.lineEdit.text()).find("PPCM") != -1:
        try:
            r = str(ui.lineEdit.text()).split(",")
            n1 = (r[0][5:])
            n2 = (r[1][:-1])
            if n1.isnumeric() and n2.isnumeric():
                n1 = int(r[0][5:])
                n2 = int(r[1][:-1])
                ui.lineEdit.setText(str(calcul_ppcm(n1, n2)))
            else:
                ui.lineEdit.setText("error PPCM")
        except:
            ui.lineEdit.setText("error PPCM")

    else:
        global ans
        global check
        try:
            ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
            ans = ui.lineEdit.text()
        except ZeroDivisionError:
            ui.lineEdit.setText("ERREUR")
        except SyntaxError:
            ui.lineEdit.setText("Opération Invalide")
        except:
            ui.lineEdit.setText("ERREUR")
        check = True


def plusmoins():
    global base
    base = 10
    check_base()
    if not (ui.lineEdit.text()):
        ui.lineEdit.setText("-")
    elif ui.lineEdit.text()[0] == "-":
        ui.lineEdit.setText(ui.lineEdit.text()[1:])
    else:
        ui.lineEdit.setText("-" + ui.lineEdit.text())


# -----------------------------------------------------------#
#                  Les fonctions predefinies                 #
# -----------------------------------------------------------#

#-------------------------------PGCD----------------------------#
def pgcd():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText("PGCD(")
    check = True

#-------------------------------CARRE----------------------------#
def carre():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(calcul_carre(eval(ui.lineEdit.text()))))
    check = False

#-------------------------------CUBE----------------------------#
def cube():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(calcul_cube(eval(ui.lineEdit.text()))))
    check = False

#-------------------------------PPCM----------------------------#
def ppcm():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText("PPCM(")
    check = True


#------------------------FACTEURS PREMIERS---------------------#
def facteur_premier():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(decompose(eval(ui.lineEdit.text()))))
    check = False

#-------------------------------FACTORIEL----------------------------#
def factoriel():
    global base
    base = 10
    check_base()
    global check
    # ui.lineEdit.setText(str(math.factorial(eval(ui.lineEdit.text()))))
    ui.lineEdit.setText(str(calcul_factoriel(eval(ui.lineEdit.text()))))
    check = False

#----------------------------------PREMIER------------------------------#
def premier():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(calcul_premier(eval(ui.lineEdit.text()))))
    check = False

#----------------------------------PARFAIT------------------------------#
def parfait():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(calcul_parfait(eval(ui.lineEdit.text()))))
    check = False
#------------------------------RACINE CARRE----------------------------#
def racine():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(math.sqrt(eval(ui.lineEdit.text()))))
    check = False
#-------------------------------TG----------------------------#
def tg():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(calcul_tg(eval(ui.lineEdit.text()))))
    check = False

#-------------------------------SIN----------------------------#
def sin():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(calcul_sin(eval(ui.lineEdit.text()))))
    check = False

#------------------------------COS---------------------------#
def cos():
    global base
    base = 10
    check_base()
    global check
    ui.lineEdit.setText(str(calcul_cos(eval(ui.lineEdit.text()))))
    check = False


# -----------------------------------------------------------#
#                     Conversion des bases                   #
# -----------------------------------------------------------#
def bin():
    global check
    global base
    try:
        if base == 10:
            ui.lineEdit.setText(str(dec_bin(eval(ui.lineEdit.text()))))
        elif base == 16:
            ui.lineEdit.setText(str(hex_bin((ui.lineEdit.text()))))
        elif base == 8:
            ui.lineEdit.setText(str(oct_bin(eval(ui.lineEdit.text()))))
        else:
            ui.lineEdit.setText((ui.lineEdit.text()))
        base = 2
        ui.b_bin.setStyleSheet("background-color: rgb(255,85,127)")
        ui.b_oct.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_dec.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_hex.setStyleSheet("background-color: rgb(255,170,255)")
        check = False
    except:
        ui.lineEdit.setText("Erreur")

def check_base():
    ui.b_dec.setStyleSheet("background-color: rgb(255,85,127)")
    ui.b_oct.setStyleSheet("background-color: rgb(255,170,255)")
    ui.b_bin.setStyleSheet("background-color: rgb(255,170,255)")
    ui.b_hex.setStyleSheet("background-color: rgb(255,170,255)")

def oct():
    global check
    global base
    try:
        if base == 10:
            ui.lineEdit.setText(str(dec_oct(eval(ui.lineEdit.text()))))
        elif base == 16:
            ui.lineEdit.setText(str(hex_oct((ui.lineEdit.text()))))
        elif base == 2:
            ui.lineEdit.setText(str(bin_oct(eval(ui.lineEdit.text()))))
        else:
            ui.lineEdit.setText((ui.lineEdit.text()))
        base = 8
        ui.b_oct.setStyleSheet("background-color: rgb(255,85,127)")
        ui.b_bin.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_dec.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_hex.setStyleSheet("background-color: rgb(255,170,255)")
        check = False
    except:
        ui.lineEdit.setText("Erreur")


def hex():
    global check
    global base
    try:
        if base == 10:
            ui.lineEdit.setText(str(dec_hex(eval(ui.lineEdit.text()))))
        elif base == 8:
            ui.lineEdit.setText(str(oct_hex(eval(ui.lineEdit.text()))))
        elif base == 2:
            ui.lineEdit.setText(str(bin_hex(eval(ui.lineEdit.text()))))
        else:
            ui.lineEdit.setText((ui.lineEdit.text()))
        base = 16
        ui.b_hex.setStyleSheet("background-color: rgb(255,85,127)")
        ui.b_bin.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_dec.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_oct.setStyleSheet("background-color: rgb(255,170,255)")
        check = False
    except:
        ui.lineEdit.setText("Erreur")


def dec():
    global check
    global base
    try:
        if base == 8:
            ui.lineEdit.setText(str(oct_dec((ui.lineEdit.text()))))
        elif base == 16:
            ui.lineEdit.setText(str(hex_dec((ui.lineEdit.text()))))
        elif base == 2:
            ui.lineEdit.setText(str(bin_dec((ui.lineEdit.text()))))
        else:
            ui.lineEdit.setText((ui.lineEdit.text()))
        base = 10
        ui.b_dec.setStyleSheet("background-color: rgb(255,85,127)")
        ui.b_bin.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_oct.setStyleSheet("background-color: rgb(255,170,255)")
        ui.b_hex.setStyleSheet("background-color: rgb(255,170,255)")
        check = False
    except:
        ui.lineEdit.setText("Erreur")
#-------------------------------------------------------------------#
#                        les connexions                             #
#-------------------------------------------------------------------#
ui.b_0.clicked.connect(zero)
ui.b_1.clicked.connect(un)
ui.b_2.clicked.connect(deux)
ui.b_3.clicked.connect(trois)
ui.b_4.clicked.connect(quatre)
ui.b_5.clicked.connect(cinq)
ui.b_6.clicked.connect(six)
ui.b_7.clicked.connect(sept)
ui.b_8.clicked.connect(huit)
ui.b_9.clicked.connect(neuf)
ui.b_plus.clicked.connect(plus)
ui.b_moins.clicked.connect(moins)
ui.b_fois.clicked.connect(fois)
ui.b_sur.clicked.connect(sur)
ui.b_plusmoins.clicked.connect(plusmoins)
ui.b_egal.clicked.connect(egal)
ui.b_point.clicked.connect(point)
ui.b_del.clicked.connect(delete)
ui.b_clear.clicked.connect(clear)
ui.b_ouvrante.clicked.connect(ouvrante)
ui.b_fermante.clicked.connect(fermante)
ui.b_virgule.clicked.connect(virgule)
ui.b_carre.clicked.connect(carre)
ui.b_cube.clicked.connect(cube)
ui.b_ppcm.clicked.connect(ppcm)
ui.b_pgcd.clicked.connect(pgcd)
ui.b_racine.clicked.connect(racine)
ui.b_fp.clicked.connect(facteur_premier)
ui.b_fact.clicked.connect(factoriel)
ui.b_premier.clicked.connect(premier)
ui.b_parfait.clicked.connect(parfait)
ui.b_tg.clicked.connect(tg)
ui.b_sin.clicked.connect(sin)
ui.b_cos.clicked.connect(cos)
ui.b_bin.clicked.connect(bin)
ui.b_oct.clicked.connect(oct)
ui.b_hex.clicked.connect(hex)
ui.b_dec.clicked.connect(dec)

sys.exit(app.exec_())
