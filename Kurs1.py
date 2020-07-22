from PyQt5 import QtCore, QtWidgets, QtGui
# Импортируем наш файл
from Kurs import Ui_MainWindow
from LinkedList import LinkedList
from Tree import BinarySearchTree
from PyQt5.QtWidgets import (QWidget, QPushButton,
QHBoxLayout, QVBoxLayout, QApplication, QListWidget, QLineEdit, QListWidgetItem,
QFileDialog)
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):#инициализация
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonSerch.clicked.connect(self.but_clicked)
        self.ui.AddTofile.clicked.connect(self.btn_clicked)
        self.ui.collect.clicked.connect(self.button_clicked)
        self.ui.clearLine.clicked.connect(self.b_clearLine)
        self.ui.clearList.clicked.connect(self.clear)
        
    def btn_clicked(self):#кнопка добавления информации о новом фильме
        #считывание текста с заполненных полей и их добавление в список
        l = []
        fil = self.ui.lineFilm2.text()
        l.append(str(fil))
        yer = self.ui.year.text()
        l.append(str(yer))
        tupe = self.ui.Type4.currentText()
        l.append(str(tupe))
        prod = self.ui.produsser.text()
        l.append(str(prod))
        if l[1].isdigit():#проверка года
            file = open('C:\\Users\\alexa\\Documents\\Films.txt', 'a',encoding = 'UTF-8')
            s = str(l[0]+", "+l[1]+", "+l[2]+", "+l[3])
            file.write(s)
            file.write("\n")
            file.close()
        else:#очистка всех полей ввода
            self.ui.lineFilm1.clear()
            self.ui.firstYear.clear()
            self.ui.secondYear.clear()
            self.ui.lineFilm2.clear()
            self.ui.year.clear()
            self.ui.produsser.clear()
        
        
    def but_clicked(self):#кнопка поиска фильма по названию
        self.ui.listFilms.clear()
        i = 0
        flag = 0
        L = LinkedList()#Объект односвязного списка
        filml = self.ui.lineFilm1.text()#Название фильма
        film = str(filml)
        file = open('C:\\Users\\alexa\\Documents\\Films.txt', 'r',encoding = 'UTF-8')
        for line in file:#добавление списков строк в односвязный список
            A = line.split(', ')
            D=dict.fromkeys([A[0]], A[1:4])
            L.add(D)
        file.close()
        while(i<L.length):#Поиск названия фильма в односвязном списке
            if L[i].get(film) is not None :
                flag+=1
                self.ui.listFilms.addItem("Название: " + film+", Жанр: "+str(L[i].get(film)[1])+
                                          ", Год выпуска: "+str(L[i].get(film)[0])+
                                          ", Режиссёр: "+str(L[i].get(film)[2]))
            i+=1
        if flag==0: 
            self.ui.listFilms.addItem("Нет совпадений")
            
    def button_clicked(self):#кнопка подбора фильмов по жанру и году
        self.ui.listFilms.clear()
        T = BinarySearchTree()#создание объекта бинарного дерева поиска
        first = 0
        second = 0
        if not self.ui.firstYear.text().isdigit():#проверка на корректный ввод года
            first = 1920
        else: first = int(self.ui.firstYear.text())
        if not self.ui.secondYear.text().isdigit():#проверка на корректный ввод года
            second = 2019
        else: second = int(self.ui.secondYear.text())
        l =[[ "аниме",[]],["фэнтези",[]],["мелодрама",[]],["биография",[]],["боевик",[]],
            ["вестерн",[]],["военный",[]],["детектив",[]],["документальный",[]],["драма",[]],
            ["мультфильм",[]],["приключения",[]],["семейный",[]], ["триллер",[]], ["ужасы",[]],
            ["фантастика",[]]]#список жанров
        file = open('C:\\Users\\alexa\\Documents\\Films.txt', 'r',encoding = 'UTF-8')
        for line in file:#добавление фильмов в список жанров
            A = line.split(', ')
            for j in range(len(l)):
                if A[2]==l[j][0]:
                    l[j][1].append(A)

        diclist = []
        for k in range(first,second+1):
            diclist.append(k)
        dic =dict.fromkeys(diclist[:])#создание словаря годов
        for k in range(first,second+1):#добавление информации в словарь
            d = []
            for j in range(len(l)):
                if(l[j][1]!=[]):
                    for q in range((len(l[j][1]))):
                        if int(l[j][1][q][1])==k:
                            d.append((l[j][1][q]))
            dic.update({int(k):d})
        for el in dic.items():#добавление элементов словаря в бинарное дерево
            T[el[0]] = el
        for que in range(first,second+1):#поиск в бинарном дереве нужного года и жанра
            if T[que][1] is not None :
                for t in range(len(T[que][1])):
                    if str(T[que][1][t][2])==self.ui.Type3.currentText():
                        self.ui.listFilms.addItem("Название: " + str(T[que][1][t][0])+", Жанр: "
                                                  +str(T[que][1][t][2])+", Год выпуска: "
                                                  +str(T[que][1][t][1])+", Режиссёр: "
                                                  +str(T[que][1][t][3]))
                    elif str(self.ui.Type3.currentText()) == "любой":
                        self.ui.listFilms.addItem("Название: " + str(T[que][1][t][0])+", Жанр: "
                                                  +str(T[que][1][t][2])+", Год выпуска: "
                                                  +str(T[que][1][t][1])+", Режиссёр: "+str(T[que][1][t][3]))
       
    def b_clearLine(self):#кнопка очистки всех полей ввода
        self.ui.lineFilm1.clear()
        self.ui.firstYear.clear()
        self.ui.secondYear.clear()
        self.ui.lineFilm2.clear()
        self.ui.year.clear()
        self.ui.produsser.clear()

    def clear(self):#нопка очистки списка
        self.ui.listFilms.clear()
        
app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()
sys.exit(app.exec())
 

