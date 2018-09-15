#```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter import font
from bouton import *
from PIL import Image, ImageTk
import os
from datetime import datetime
class Ui_MainWindow(Frame):
	'''
	GUI de l'application
	'''
	def __init__(self,MainWindow):
		'''
		Unique et principale fonction, sans méthodes
		'''
		
		#Création d'un fichier qui contient l'historique des calculs
		historique = open("historique.txt","a")
		historique.write("----------"+str(datetime.now())+"---------- \n")

		#Chaine de caractère variable utiliser pour les différents label
		calcul = StringVar()
		result = StringVar()
		mode = StringVar()
		result2 = StringVar()

		#Indique que le mode pa défaut de la calculatrice est en Radians, en attribuant à la variable mode la chaîne de caractère  "RAD"
		mode.set("RAD")

		#Formatage du texte, police et taille
		fontecran=font.Font(family='Microsoft JhengHei UI Light', size=19)
		font1=font.Font(size=17)
		font2=font.Font(size=12)

		#Affiche PY calculator dans la fénetre
		titre = Label(MainWindow, text="PY CALCULATOR",padx=5, pady=10, width=331,  font = fontecran, anchor=CENTER).pack()

		#Ecran de la calculatrice
		Ecran = Frame(MainWindow, borderwidth=2, relief=FLAT, width=391, height=221, bg='ivory')
		#Création de 3 Labels contenant des chaîne de caractère vide
		Label1 = Label(Ecran, textvariable=calcul,padx=5, pady=15, width=331, bg='ivory', font = fontecran, anchor=W).pack()
		Label2 = Label(Ecran, textvariable=result,padx=5, pady=0, width=331, bg='ivory', font = fontecran, anchor=E).pack()
		Label3 = Label(Ecran, textvariable=result2,padx=5, pady=0, width=331, bg='ivory', font = fontecran, anchor=N).pack()
		self.mode = Label(Ecran, textvariable = mode, bg ='gray25', foreground ='white', font="-weight bold").place(width =36, height=20)
		Ecran.place(y= 50, x=-6)
		Ecran.pack_propagate(False) #Empeche la redimension de l'écran
		

		def update_graphe(calcul):
			'''
			Affiche un graphique dans l'écran
			'''
			try:
				appui_graphe(calcul,result) #Fonction qui met à jour l'image du graphique dans le dossier
				#Conversion de l'image en iune image interprétable par Tkinter
				myFile = "fig.png"
				image = Image.open(myFile)
				photo = ImageTk.PhotoImage(image)
				graphique = Label(MainWindow, image = photo)
				graphique.image = photo
				#Placement de l'image
				graphique.place(x =-4, y =50, width=391,height=221)
				#Création d'un second bouton quit (par dessus du quit) qui permet à l'utilisateur de supprimer l'affichage du graphique à l'écran
				quit2 = Button(MainWindow, text = 'quit', relief=FLAT, background = 'red2', activebackground='red3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_quit2(calcul,graphique,quit2))
				quit2.place(x = 296, y = 284, width=63, height=33)
				def appui_quit2(calcul,graphique,quit2):
					'''
					Une fonction qui permet au bouton quit2 de supprimer et de e supprimer lui même l'orsque l'on appuie dessus
					'''
					quit2.destroy()
					graphique.destroy()
			except:
				calcul.set("Erreur de Syntaxe")

		#Affichage de l'écran  pour faire des calculs sur les fonctions
		Ecran_calcul = Frame(MainWindow, borderwidth=2, relief=FLAT, width=391, height=221, bg='ivory')
		image = Button(Ecran_calcul, text = 'Calculer une image', relief=FLAT, background = 'DodgerBlue2', activebackground='DodgerBlue3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_image(result,Ecran_calcul))
		image.place(x = 0, y = 30, width=391, height=33)
		deriv = Button(Ecran_calcul, text = "Calculer l'expréssion de la dérivé", relief=FLAT, background = 'DodgerBlue2', activebackground='DodgerBlue3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_deriv(calcul,result,Ecran_calcul))
		deriv.place(x = 0, y = 90, width=391, height=33)
		
		#Ajouter les boutons + et - l'infini pour le calcul de limite
		infinimoins = Button(MainWindow, text = '-∞', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_infinimoins(result))
		infini = Button(MainWindow, text = '+∞', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_infini(result))
		limite = Button(Ecran_calcul, text = "Calculer une limite", relief=FLAT, background = 'DodgerBlue2', activebackground='DodgerBlue3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_limite(result, Ecran_calcul,infini,infinimoins))
		limite.place(x = 0, y = 150, width=391, height=33)


		#Bouton
		self.fx = Button(MainWindow, text = 'f(x)=', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0, cursor ='hand1',command = lambda: appui_fx(calcul))
		self.fx.place(x = 16, y = 284, width=136, height=33)
		self.graphe = Button(MainWindow, text = 'graphe', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0,cursor ='hand1',command = lambda: update_graphe(calcul))
		self.graphe.place(x = 158, y = 284, width=63, height=33)
		self.calcul = Button(MainWindow, text = 'calcul', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0, cursor = 'hand1',command = lambda: appui_calcul(calcul,Ecran_calcul))
		self.calcul.place(x = 227, y = 284, width=63, height=33)
		self.quit = Button(MainWindow, text = 'quit', relief=FLAT, background = 'red2', activebackground='red3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_quit(Ecran_calcul,result,result2))
		self.quit.place(x = 296, y = 284, width=63, height=33)
		self.apps = Button(MainWindow, text = 'apps', relief=FLAT, background = 'DodgerBlue2', activebackground='DodgerBlue3',borderwidth=0, cursor ='hand1', foreground = 'white')
		self.apps.place(x = 16, y = 320, width=63, height=33)
		self.radian = Button(MainWindow, text = 'radian', relief=FLAT, background = 'DodgerBlue2', activebackground='DodgerBlue3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_radian(mode))
		self.radian.place(x = 89, y = 320, width=63, height=33)
		self.degre = Button(MainWindow, text = 'degré', relief=FLAT, background = 'DodgerBlue2', activebackground='DodgerBlue3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_degre(mode))
		self.degre.place(x = 159, y = 320, width=63, height=33)
		self.xvariable = Button(MainWindow, text = 'x', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0, cursor = 'hand1',command = lambda: appui_xvariable(calcul))
		self.xvariable.place(x = 227, y = 320, width=63, height=33)
		self.suppr = Button(MainWindow, text = 'suppr', relief=FLAT, background = 'red2', activebackground='red3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_suppr(calcul,result))
		self.suppr.place(x = 296, y = 320, width=63, height=33)
		self.xpuissancemoins1 = Button(MainWindow, text = 'x^(-1)', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_xpuissancemoins1(calcul,result))
		self.xpuissancemoins1.place(x = 16, y = 356, width=63, height=33)
		self.sinus = Button(MainWindow, text = 'sin', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_sinus(calcul,result))
		self.sinus.place(x = 89, y = 356, width=63, height=33)
		self.cosinus = Button(MainWindow, text = 'cos', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_cosinus(calcul,result))
		self.cosinus.place(x = 159, y = 356, width=63, height=33)
		self.tangente = Button(MainWindow, text = 'tan', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_tangente(calcul,result))
		self.tangente.place(x = 227, y = 356, width=63, height=33)
		self.piconstante = Button(MainWindow, text = 'π', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_piconstante(calcul,result))
		self.piconstante.place(x = 296, y = 356, width=63, height=33)
		self.puissance = Button(MainWindow, text = '^', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_puissance(calcul,result))
		self.puissance.place(x = 16, y = 393, width=63, height=33)
		self.racine = Button(MainWindow, text = '√', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_racine(calcul,result))
		self.racine.place(x = 89, y = 393, width=63, height=33)
		self.x2 = Button(MainWindow, text = 'x^2', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_x2(calcul,result))
		self.x2.place(x = 159, y = 393, width=63, height=33)
		self.paren1 = Button(MainWindow, text = '(', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_paren1(calcul,result))
		self.paren1.place(x = 227, y = 393, width=63, height=33)
		self.paren2 = Button(MainWindow, text = ')', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_paren2(calcul,result))
		self.paren2.place(x = 296, y = 393, width=63, height=33)
		self.arrondi = Button(MainWindow, text = 'arrondi', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_arrondi(calcul,result))
		self.arrondi.place(x = 16, y = 429, width=63, height=33)
		self.x10 = Button(MainWindow, text = '10^x', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_x10(calcul,result))
		self.x10.place(x = 89, y = 429, width=63, height=33)
		self.ex = Button(MainWindow, text = 'e^x', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_ex(calcul,result))
		self.ex.place(x = 159, y = 429, width=63, height=33)
		self.racinecubique = Button(MainWindow, text = '∛', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1', font = font1,command = lambda: appui_racinecubique(calcul,result))
		self.racinecubique.place(x = 227, y = 429, width=63, height=33)
		self.log1 = Button(MainWindow, text = 'log', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_log1(calcul,result))
		self.log1.place(x = 16, y = 467, width=63, height=33)
		self.ln1 = Button(MainWindow, text = 'ln', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_ln1(calcul,result))
		self.ln1.place(x = 16, y = 503, width=63, height=33)
		self.rep = Button(MainWindow, text = 'rep', relief=FLAT, background = 'cornsilk2', activebackground='cornsilk3',borderwidth=0, cursor = 'hand1',command = lambda: appui_rep(calcul,result))
		self.rep.place(x = 16, y = 540, width=63, height=33)
		self.aide = Button(MainWindow, text = '?', relief=FLAT, background = 'chartreuse2', activebackground='chartreuse3',borderwidth=0, cursor ='hand1', foreground = 'white')
		self.aide.place(x = 16, y = 576, width=63, height=33)
		self.division = Button(MainWindow, text = '÷', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0, cursor = 'hand1', font = font2,command = lambda: appui_division(calcul,result))
		self.division.place(x = 296, y = 429, width=63, height=33)
		self.multipli = Button(MainWindow, text = '×', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0, cursor = 'hand1', font = font2,command = lambda: appui_multipli(calcul,result))
		self.multipli.place(x = 296, y = 467, width=63, height=33)
		self.moins = Button(MainWindow, text = '-', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0, cursor = 'hand1', font = font2,command = lambda: appui_moins(calcul,result))
		self.moins.place(x = 296, y = 503, width=63, height=33)
		self.plus = Button(MainWindow, text = '+', relief=FLAT, background = 'ghost white', activebackground='gainsboro',borderwidth=0, cursor = 'hand1', font = font2,command = lambda: appui_plus(calcul,result))
		self.plus.place(x = 296, y = 540, width=63, height=33)
		self.entrer = Button(MainWindow, text = 'enter', relief=FLAT, background = 'red2', activebackground='red3',borderwidth=0, cursor ='hand1', foreground = 'white',command = lambda: appui_entrer(calcul,result,mode,result2,historique))
		self.entrer.place(x = 296, y = 576, width=63, height=33)
		self.num7 = Button(MainWindow, text = '7', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_7(calcul,result))
		self.num7.place(x = 89, y = 470, width=63, height=41)
		self.num8 = Button(MainWindow, text = '8', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_8(calcul,result))
		self.num8.place(x = 159, y = 470, width=63, height=41)
		self.num9 = Button(MainWindow, text = '9', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_9(calcul,result))
		self.num9.place(x = 227, y = 470, width=63, height=41)
		self.num4 = Button(MainWindow, text = '4', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_4(calcul,result))
		self.num4.place(x = 89, y = 515, width=63, height=41)
		self.num5 = Button(MainWindow, text = '5', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_5(calcul,result))
		self.num5.place(x = 159, y = 515, width=63, height=41)
		self.num6 = Button(MainWindow, text = '6', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_6(calcul,result))
		self.num6.place(x = 227, y = 515, width=63, height=41)
		self.num1 = Button(MainWindow, text = '1', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2, command = lambda: appui_1(calcul,result))
		self.num1.place(x = 89, y = 560, width=63, height=41)
		self.num2 = Button(MainWindow, text = '2', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_2(calcul,result))
		self.num2.place(x = 159, y = 560, width=63, height=41)
		self.num3 = Button(MainWindow, text = '3', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_3(calcul,result))
		self.num3.place(x = 227, y = 560, width=63, height=41)
		self.num0 = Button(MainWindow, text = '0', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_0(calcul,result))
		self.num0.place(x = 89, y = 605, width=63, height=41)
		self.virgule = Button(MainWindow, text = '.', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_virgule(calcul,result))
		self.virgule.place(x = 159, y = 605, width=63, height=41)
		self.nega = Button(MainWindow, text = '(-)', relief=FLAT, background = 'SlateGray3', activebackground='SlateGray4',borderwidth=0,cursor ='hand1', font = font2,command = lambda: appui_nega(calcul,result))
		self.nega.place(x = 227, y = 605, width=63, height=41)
		MainWindow.mainloop()
