from math import *
from time import sleep
from tkinter import *
from pylab import linspace,figure,plot,grid,title,savefig, plt
from PIL import Image, ImageTk
import numpy as np
from sympy import symbols, ln, diff, limit
'''
Toutes les commandes des boutons
if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
est utilisé pour reintaliser la valeur d'une variable après une erreur de syntaxte
'''
def appui_1(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"1")
	else:
		calcul.set(calcul.get()+"1")
def appui_2(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"2")
	else:
		calcul.set(calcul.get()+"2")
def appui_3(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"3")
	else:
		calcul.set(calcul.get()+"3")
def appui_4(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"4")
	else:
		calcul.set(calcul.get()+"4")
def appui_5(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"5")
	else:
		calcul.set(calcul.get()+"5")
def appui_6(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"6")
	else:
		calcul.set(calcul.get()+"6")
def appui_7(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"7")
	else:
		calcul.set(calcul.get()+"7")
def appui_8(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"8")
	else:
		calcul.set(calcul.get()+"8")
def appui_9(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"9")
	else:
		calcul.set(calcul.get()+"9")
def appui_0(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"0")
	else:
		calcul.set(calcul.get()+"0")
def appui_xpuissancemoins1(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"^(-1)")
	else:
		calcul.set(calcul.get()+"^(-1)")
def appui_sinus(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"sin(")
	else:
		calcul.set(calcul.get()+"sin(")
def appui_cosinus(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"cos(")
	else:
		calcul.set(calcul.get()+"cos(")
def appui_tangente(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"tan(")
	else:
		calcul.set(calcul.get()+"tan(")
def appui_piconstante(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"π")
	else:
		calcul.set(calcul.get()+"π")
def appui_puissance(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"^")
	else:
		calcul.set(calcul.get()+"^")
def appui_racine(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"√(")
	else:
		calcul.set(calcul.get()+"√(")
def appui_x2(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"^2")
	else:
		calcul.set(calcul.get()+"^2")
def appui_paren1(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"(")
	else:
		calcul.set(calcul.get()+"(")
def appui_paren2(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+")")
	else:
		calcul.set(calcul.get()+")")
def appui_arrondi(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"arrondi(")
	else:
		calcul.set(calcul.get()+"arrondi(")
def appui_x10(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"10^(")
	else:
		calcul.set(calcul.get()+"10^(")
def appui_ex(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"e^(")
	else:
		calcul.set(calcul.get()+"e^(")
def appui_racinecubique(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"∛(")
	else:
		calcul.set(calcul.get()+"∛(")
def appui_log1(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"log(")
	else:
		calcul.set(calcul.get()+"log(")
def appui_ln1(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"ln(")
	else:
		calcul.set(calcul.get()+"ln(")
def appui_rep(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if result.get() != "":
		calcul.set(calcul.get()+"rep")
def appui_division(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"÷")
	else:
		calcul.set(calcul.get()+"÷")
def appui_multipli(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"×")
	else:
		calcul.set(calcul.get()+"×")
def appui_moins(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"-")
	else:
		calcul.set(calcul.get()+"-")
def appui_plus(calcul,result):
	if calcul.get()=="Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"+")
	else:
		calcul.set(calcul.get()+"+")
def appui_virgule(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+".")
	else:
		calcul.set(calcul.get()+".")
def appui_nega(calcul,result):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if "Entrer l'image à calculer : " in result.get() or "Limite de f(x) en : "in result.get():
		result.set(result.get()+"-")
	else:
		calcul.set(calcul.get()+"-")
def appui_fx(calcul):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	calcul.set("f(x)=")
def appui_xvariable(calcul):
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	calcul.set(calcul.get()+"x")
def appui_suppr(calcul,result):
	'''
	Si la chaine de caractère fini par cos( par exemple, on supprime les 4 dernier caratère de la chaîne
	'''
	if calcul.get()== "Erreur de Syntaxe":
		calcul.set("")
	if calcul.get().endswith ('tan(') or calcul.get().endswith ('sin(') or calcul.get().endswith ('sin(') or calcul.get().endswith ('10^(') or calcul.get().endswith ('log(') or calcul.get().endswith ('cos('):
		calcul.set(calcul.get()[:-4])
	elif calcul.get().endswith ('^(-1)') or calcul.get().endswith ('f(x)='):
		calcul.set(calcul.get()[:-5])
	elif calcul.get().endswith ('arrondi('):
		calcul.set(calcul.get()[:-8])
	elif calcul.get().endswith ('^2') or calcul.get().endswith ('∛(') or calcul.get().endswith ('√('):
		calcul.set(calcul.get()[:-2])
	elif calcul.get().endswith ('e^(') or calcul.get().endswith ('ln(') or calcul.get().endswith ('rep'):
		calcul.set(calcul.get()[:-3])
	else:
		calcul.set(calcul.get()[:-1])
def appui_radian(mode):
	mode.set("RAD")
def appui_degre(mode):
	mode.set("DEG")

def appui_entrer(calcul,result,mode,result2,historique):
	'''
	Fonction pour les principaux calculs:
	Opération
	Calcul d'image
	Calcule de limite
	'''
	if "Entrer l'image à calculer : " in result.get():
		#On récupère la valeur du texte saisi au clavier de la calcultrice par l'utilisateur
		a = calcul.get()
		#On remplace certains caractère de la chaine pour rendre compréhensible la saisi de l'utilisateur par l'intrpréteur python
		a = a.replace('×','*')
		a = a.replace('^','**')
		a = a.replace('√','sqrt')
		a = a.replace('arrondi','ceil')
		a = a.replace('π','pi')
		a = a.replace('∛','sqrtcub')
		a = a.replace('ln','log')
		a = a.replace('log10','logartihme_10')
		a = a.replace('rep',result.get())
		a = a.replace('f(x)=','')
		b=""
		#fonction qui ajoute des "*" entre une lettre et un  chiffre, exemple: si l'utilisateur entre  5cos(2) dans la calculatrice, cette chaîne seras transformer en 5*cos(2)
		for i in range (len(a)-1):
			b+= a[i]
			if a[i].isalpha() and a[i+1].isdigit() or a[i].isdigit() and a[i+1].isalpha():
				b= b+"*"
		b = b + a[-1]
		#fonction qui refermeles parenthèse que l'utilisateur aurait pue oublier de réfermer
		paren1 = b.count("(")
		paren2 = b.count(")")
		if paren1 > paren2:
			nbrdeparen = paren1 - paren2
			b += nbrdeparen*(")")
		print(b)
		try:
			x= result.get()
			x = x.replace("Entrer l'image à calculer : ","")
			x = eval(x)
			#On évalue la fonction
			result2.set(str(eval(b)))
		except:
			sleep(3)
			calcul.set("Erreur de Syntaxe")

	elif "Limite de f(x) en : "in result.get():
		a = calcul.get()
		a = a.replace('×','*')
		a = a.replace('^','**')
		a = a.replace('√','sqrt')
		a = a.replace('arrondi','ceil')
		a = a.replace('π','pi')
		a = a.replace('∛','sqrtcub')
		a = a.replace('ln','log')
		a = a.replace('log10','logartihme_10')
		a = a.replace('rep',result.get())
		a = a.replace('f(x)=','')
		b=""
		for i in range (len(a)-1):
			b+= a[i]
			if a[i].isalpha() and a[i+1].isdigit() or a[i].isdigit() and a[i+1].isalpha():
				b= b+"*"
		b = b + a[-1]
		paren1 = b.count("(")
		paren2 = b.count(")")
		if paren1 > paren2:
			nbrdeparen = paren1 - paren2
			b += nbrdeparen*(")")
		print(b)
		limite = result.get()
		limite = limite.replace("Limite de f(x) en : ", "")		
		limite = limite.replace("∞","oo")
		x = symbols('x')
		try:	
			limitefx = str(limit(b,x,limite))
			limitefx = limitefx.replace("oo","∞")
			result2.set(str(limitefx))
		except:
			sleep(3)
			calcul.set("Erreur de Syntaxe")


	else:
		a = calcul.get()
		a = a.replace('×','*')
		a = a.replace('^','**')
		a = a.replace('√','sqrt')
		a = a.replace('arrondi','ceil')
		a = a.replace('π','pi')
		a = a.replace('∛','sqrtcub')
		a = a.replace('ln','log')
		a = a.replace('log10','logartihme_10')
		a = a.replace('rep',result.get())
		if mode.get()=="DEG":
			a = a.replace("cos","cos(radians(")
			a = a.replace("tan","tan(radianss(")
			a = a.replace("sin","sin(radians(")
		b=""
		for i in range (len(a)-1):
			b+= a[i]
			if a[i].isalpha() and a[i+1].isdigit() or a[i].isdigit() and a[i+1].isalpha():
				b= b+"*"
		b = b + a[-1]
		paren1 = b.count("(")
		paren2 = b.count(")")
		if paren1 > paren2:
			nbrdeparen = paren1 - paren2
			b += nbrdeparen*(")")
		print(b)
		try:
			result.set(str(eval(b)))
			rep = str(eval(b))
			print(rep)
			historique.write(b+"\n")
			historique.write(rep+"\n")
			calcul.set("")
		except:
			sleep(3)
			calcul.set("Erreur de Syntaxe")
def appui_graphe(calcul,result):
	'''
	Fonction qui crée un graphique avec la fonction entrée par l'utilisateur
	'''
	if "f(x)=" in calcul.get():
		a = calcul.get()
		a = a.replace('f(x)=','')
		a = a.replace('×','*')
		a = a.replace('^','**')
		a = a.replace('√','sqrt')
		a = a.replace('arrondi','ceil')
		a = a.replace('π','pi')
		a = a.replace('∛','sqrtcub')
		a = a.replace('ln','log')
		a = a.replace('log10','logartihme_10')
		a = a.replace('rep',result.get())
		a = a.replace('cos','np.cos')
		a = a.replace('sin','np.sin')
		a = a.replace('sin','np.sin')
		a = a.replace("f'(x)= ","")
		b=""
		for i in range (len(a)-1):
			b+= a[i]
			if a[i].isalpha() and a[i+1].isdigit() or a[i].isdigit() and a[i+1].isalpha():
				b= b+"*"
		b = b + a[-1]
		paren1 = b.count("(")
		paren2 = b.count(")")
		if paren1 > paren2:
			nbrdeparen = paren1 - paren2
			b += nbrdeparen*(")")
		print(b)
		try:
			#Création et sauvegarde du graphqique sous forme d'une image
			x = np.linspace(0, 2*pi, 30)
			y = eval(b)
			plt.figure(figsize=(4.2,2.1))
			plot(x, y)
			grid(True)
			title(calcul.get())
			savefig('fig.png', bbox_inches='tight')

		except:
			sleep(3)
			calcul.set("Erreur de Syntaxe")


def appui_deriv(calcul,result,Ecran_calcul):
	'''
	Calcul de l'expression de la dérivé
	'''
	if "f(x)=" in calcul.get():
		a = calcul.get()
		a = a.replace('f(x)=','')
		a = a.replace('×','*')
		a = a.replace('^','**')
		a = a.replace('√','sqrt')
		a = a.replace('arrondi','ceil')
		a = a.replace('π','pi')
		a = a.replace('∛','sqrtcub')
		a = a.replace('ln','log')
		a = a.replace('log10','logartihme_10')
		a = a.replace('rep',result.get())
		a = a.replace('cos','np.cos')
		a = a.replace('sin','np.sin')
		a = a.replace('sin','np.sin')

		b=""
		for i in range (len(a)-1):
			b+= a[i]
			if a[i].isalpha() and a[i+1].isdigit() or a[i].isdigit() and a[i+1].isalpha():
				b= b+"*"
		b = b + a[-1]
		paren1 = b.count("(")
		paren2 = b.count(")")
		if paren1 > paren2:
			nbrdeparen = paren1 - paren2
			b += nbrdeparen*(")")
		print(b)
		try:
			x = symbols('x')
			#fonction qui calcul la dérivé
			b = str(diff(eval(b),x))
			result.set("f'(x)= "+ b)
			Ecran_calcul.place_forget()
			calcul.set("")
		except:
			sleep(3)
			calcul.set("Erreur de Syntaxe")

def appui_infini(result):
	result.set(result.get()+"+∞")

def appui_infinimoins(result):
	result.set(result.get()+"-∞")

def appui_image(result, Ecran_calcul):
	#Modifie le label 1 pour la condition dans la fonction appui_entrer
	result.set("Entrer l'image à calculer : ")
	Ecran_calcul.place_forget()

def appui_limite(result, Ecran_calcul,infini,infinimoins):
	#Modifie le label 1 pour la condition dans la fonction appui_entrer
	result.set("Limite de f(x) en : ")
	#Placement des bouton + et moins l'infini
	infinimoins.place(x = 16, y = 610, width=63, height=33)
	infini.place(x = 296, y = 610, width=63, height=33)
	Ecran_calcul.place_forget()

def appui_calcul(calcul,Ecran_calcul):
	"""
	Place l'écran de calcul sur les fonctions
	"""
	if "f(x)=" in calcul.get():
		Ecran_calcul.place(y= 50, x=-6)

def appui_quit(Ecran_calcul,result,result2):
	#Sert à réintalliser la calculatrice
	Ecran_calcul.place_forget()
	result.set("")
	result2.set('')

	
def sqrtcub(nbr):
	'''
	Fonction racine cubique
	'''
	nbr = nbr**(1/3)
	return nbr
def logartihme_10(nbr):
	'''
	FGonction logarithme en base 10
	'''
	nbr = log10(nbr)
	return nb
