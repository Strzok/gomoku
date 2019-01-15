# -*- coding: utf-8 -*-

from django.shortcuts import render
from game.models import Coord_o 
from game.models import Coord_x
from game.models import Difficulty_level
from django.http import HttpRequest
from django.contrib.postgres.fields import ArrayField

# Create your views here.

def index(request):
    return render(request, 'game/index.html',{})

def result(request, number):
    client_ip = request.META.get("REMOTE_ADDR")#pobiera ip
    result = 759
    if number == 'size10' or number == 'size15' or number == 'size20' or number == 'size25' :
        print ("zmiana poziomu")
 

        number = '0'
    if number == '0':
 
        try:  
            e = Coord_x.objects.filter(ip = client_ip).delete()
        except Coord_x.DoesNotExist:
            q = Coord_x(ip = client_ip, coord_xx = '0', coord_xy = '0')  
            q.save()
        try:
            f = Coord_o.objects.filter(ip = client_ip).delete() 
        except Coord_o.DoesNotExist:
            p = Coord_o(ip = client_ip, coord_ox = '0', coord_oy = '0')#tworzy wpis
            p.save()
        try:
            g = Difficulty_level.objects.get(ip = client_ip)
        except Difficulty_level.DoesNotExist:
            h = Difficulty_level(ip = client_ip, level_in_model = '3')
            h.save()
                
   
    else:
        try:
            Coord_o.objects.get(ip = client_ip)#pobiera z bazy o dla podanego ip
        except Coord_o.DoesNotExist:
            p = Coord_o(ip = client_ip, coord_ox = '0', coord_oy = '0')#tworzy wpis
            p.save()      
        try:
            Coord_x.objects.get(ip = client_ip)#pobiera z bazy x dla podanego ip
        except Coord_x.DoesNotExist:
            q = Coord_x(ip = client_ip, coord_xx = '0', coord_xy = '0')  
            q.save()
        try:
            Difficulty_level.objects.get(ip = client_ip)
        except Difficulty_level.DoesNotExist:
            h = Difficulty_level(ip = client_ip, level_in_model = '3')  
            h.save()


        coord_o = Coord_o.objects.get(ip = client_ip)     #wyciaga rekord z danymi rucho komptera  
        coord_x = Coord_x.objects.get(ip = client_ip)

        difficulty_level =  Difficulty_level.objects.get(ip = client_ip)
        difficulty_level.save
        level = difficulty_level.level_in_model

        coord_o.save
        coord_x.save
        list_ox = []#deklaruje listy 
        list_oy = []
        list_xx = []
        list_xy = []
    
        list_ox = coord_o.coord_ox #lista wspolrzednych ruchu komptera po xach
        list_oy = coord_o.coord_oy #lista wspolrzednych ruchu komptera po yach
        list_xx = coord_x.coord_xx
        list_xy = coord_x.coord_xy

        list_ox = list_ox.split(' ')#rozbija pobrane zmienne w formie str na list
        list_oy = list_oy.split(' ')
        list_xx = list_xx.split(' ')
        list_xy = list_xy.split(' ')

        print (list_ox[0])
        print (type(list_ox)) 
        print (list_ox)
        print (list_xx)
        print (coord_o.coord_ox[1:4])
        result = 548
        number = float(number)
        rest_of_modulo_of_number = number%1
        if rest_of_modulo_of_number != 0:
            level_float = (number%1) * 10
            level_float = int(level_float)
            level = str(level_float)
            h = Difficulty_level(ip = client_ip, level_in_model = level)
            h.save()

        print ("level:" + level)
        print (number)
        number = number - (number%1)
        kolumna = number%100
        wiersz = (number-kolumna)/100
        kolumna = int(kolumna)
        wiersz = int(wiersz)
        kolumna = kolumna-1
        wiersz = wiersz-1
        liczba_pol = 10
        tabg = [['-'for col in range(liczba_pol+5)]for row in range(liczba_pol+5)]
        tabg[wiersz][kolumna] = 'X'
 
        for i in range(1,len(list_xy)):#zamienia listy strinow na listy integerow
            
            list_xy[i] = int(list_xy[i])
            list_xx[i] = int(list_xx[i])  
        for i in range(1,len(list_xy)):#wypelnia tabg Xami w polach w ktorych krzyzyk postawil zawodnik
        	tabg[list_xy[i]][list_xx[i]] = 'X'
        print (tabg)
        if list_xx:
            list_xx.append(kolumna)#dodaje wspolrz ostaiego ruchu gracza do list
            list_xy.append(wiersz)
            list_xx = ' '.join(map(str, list_xx))#laczy listy w str
            list_xy = ' '.join(map(str, list_xy))
            p = Coord_x(ip = client_ip, coord_xx = list_xx, coord_xy = list_xy)#wrzuca listy do bazy danych
            p.save()
            p.coord_xx


        for i in range(1,len(list_oy)):#zamienia listy strinow na listy integerow
        
            list_oy[i] = int(list_oy[i])
            list_ox[i] = int(list_ox[i])  
        for i in range(1,len(list_oy)):#wypelnia tabg Oami w polach w ktorych kolko postawil komp
        	tabg[list_oy[i]][list_ox[i]] = 'O'
        print (tabg) 




        komputer_rozpoczyna = False
        a = False
        if komputer_rozpoczyna == True:
            tabg[liczba_pol/2][liczba_pol/2] = 'O'
        wygrana_gracza = False
        wygrana_komputera = False
        decyzja_komputera = False
        # if wygrana_gracza == False and wygrana_komputera == False:

        for i in range(liczba_pol):
            for j in range(liczba_pol):
    	        if tabg[i][j]=='X' and tabg[i][j+1]=='X' and tabg[i][j+2]=='X' and tabg[i][j+3]=='X' and tabg[i][j+4]=='X':
                    wygrana_gracza = True
              	if tabg[i][j]=='X' and tabg[i+1][j+1]=='X' and tabg[i+2][j+2]=='X' and tabg[i+3][j+3]=='X' and tabg[i+4][j+4]=='X':        
                    wygrana_gracza = True
                if tabg[i][j]=='X' and tabg[i+1][j]=='X' and tabg[i+2][j]=='X' and tabg[i+3][j]=='X' and tabg[i+4][j]=='X':
                    wygrana_gracza = True
                if j>3:
                    if tabg[i][j]=='X' and tabg[i+1][j-1]=='X' and tabg[i+2][j-2]=='X' and tabg[i+3][j-3]=='X' and tabg[i+4][j-4]=='X':
               	        wygrana_gracza = True
 
        if a==a and wygrana_gracza == False:
            if a==a:
                if a==a:
                    if a==a:
                        tabk = [['-','O','O','O','O','Z','0','Z','Q'],
                        ['O','O','O','O','-','Z','4','Z','Q'],
                        ['O','-','O','O','O','Z','1','Z','Q'],
                        ['O','O','-','O','O','Z','2','Z','Q'],
                        ['O','O','O','-','O','_','3','_','Q'],
                        ['-','X','X','X','X','_','0','_','W'],
                        ['X','X','X','X','-','_','4','_','W'],
                        ['X','-','X','X','X','_','1','_','W'],
                        ['X','X','-','X','X','_','2','_','W'],
                        ['X','X','X','-','X','_','3','_','W'],
                        ['-','O','O','O','-','-','4','_','E'],
                        ['-','-','O','O','O','-','1','_','E'],
                        ['-','O','O','-','O','-','3','_','E'],
                        ['-','O','-','O','O','-','2','_','E'],
                        ['-','X','X','X','-','-','4','_','R'],
                        ['-','-','X','X','X','-','1','_','R'],
                        ['-','X','X','-','X','-','3','_','R'],
                        ['-','X','-','X','X','-','2','_','R'],
                        ['-','-','O','O','O','_','1','_','T'],
                        ['-','O','O','O','-','_','0','_','T'],
                        ['O','O','O','-','-','_','3','_','T'],
                        ['-','O','-','O','O','_','2','_','T'],
                        ['-','O','O','-','O','_','3','_','T'],
                        ['O','O','-','O','-','_','2','_','T'],
                        ['O','-','O','O','-','_','1','_','T'],
                        ['O','-','-','O','O','_','2','_','T'],
                        ['O','O','-','-','O','_','3','_','T'],
                        ['-','-','X','X','X','_','1','_','Y'],
                        ['-','X','X','X','-','_','0','_','Y'],
                        ['X','X','X','-','-','_','3','_','Y'],
                        ['-','X','-','X','X','_','2','_','Y'],
                        ['-','X','X','-','X','_','3','_','Y'],
                        ['X','X','-','X','-','_','2','_','Y'],
                        ['X','-','X','X','-','_','1','_','Y'],
                        ['X','-','-','X','X','_','2','_','Y'],
                        ['X','X','-','-','X','_','3','_','Y'],
                        ['O','O','-','-','-','_','2','_','U'],
                        ['-','-','O','O','-','_','1','_','U'],
                        ['-','-','-','O','O','_','2','_','U'],
                        ['O','-','O','-','-','_','1','_','U'],
                        ['-','O','-','O','-','_','2','_','U'],
                        ['-','-','O','-','O','_','3','_','U'],
                        ['O','-','-','O','-','_','1','_','U'],
                        ['-','O','-','-','O','_','2','_','U'],
                        ['X','X','-','-','-','_','2','_','I'],
                        ['-','-','X','X','-','_','1','_','I'],
                        ['-','-','-','X','X','_','2','_','I'],
                        ['X','-','X','-','-','_','1','_','I'],
                        ['-','X','-','X','-','_','2','_','I'],
                        ['-','-','X','-','X','_','3','_','I'],
                        ['X','-','-','X','-','_','1','_','I'],
                        ['-','X','-','-','X','_','2','_','I'],
                        ['-','-','X','-','-','_','1','_','O'],
                        ['-','-','O','-','-','_','1','_','P']]
                        waga = 0
                        l = 0
                        imax = 0 #wspolrzedna pola w najwyzsza wartoscia priorytetu
                        jmax = 0 #wspolrzedna pola w najwyzsza wartoscia priorytetu
                        tabl = [[ 0 for col in range(liczba_pol+5)]for row in range(liczba_pol+5)]
                        for i in range(liczba_pol):
            	            for j in range(liczba_pol):
                                for k in range(54):
                        	    if tabk[k][8]=='Q':
                                        waga = 3750000
                                    elif tabk[k][8]=='W':
                                        waga = 750000
                        	    elif tabk[k][8]=='E':
                                        waga = 150000
            	                    elif tabk[k][8]=='R' and level == '4':
                                        waga = 30000
                	            elif tabk[k][8]=='T' and level == '4':
                                        waga = 3000
                                    elif tabk[k][8]=='Y' and level == '4':
                                        waga = 300
                                    elif tabk[k][8]=='U' and level == '4':
                                        waga = 30
                            	    elif tabk[k][8]=='I' and level == '4':
                                        waga = 3
                        	    elif tabk[k][8]=='O' and level == '4':
                                        waga = 2
                                    elif tabk[k][8]=='U' and level == '3':
                                        waga = 1
                            	    elif tabk[k][8]=='I' and level == '3':
                                        waga = 1
                        	    elif tabk[k][8]=='O' and level == '3':
                                        waga = 1
                                    elif tabk[k][8]=='Y' and level == '2':
                                        waga = 1
                                    elif tabk[k][8]=='U' and level == '2':
                                        waga = 1
                            	    elif tabk[k][8]=='I' and level == '2':
                                        waga = 1
                        	    elif tabk[k][8]=='O' and level == '2':
                                        waga = 1
                       	            elif tabk[k][8]=='E' and level == '1':
                                        waga = 1
            	                    elif tabk[k][8]=='R' and level == '1':
                                        waga = 1
                	            elif tabk[k][8]=='T' and level == '1':
                                        waga = 1
                                    elif tabk[k][8]=='Y' and level == '1':
                                        waga = 1
                                    elif tabk[k][8]=='U' and level == '1':
                                        waga = 1
                            	    elif tabk[k][8]=='I'and level == '1':
                                        waga = 2
                        	    elif tabk[k][8]=='O'and level == '1':
                                        waga = 2
                               	    elif tabk[k][8]=='P':
                                        waga = 1
                        	    else:
                                        waga = 0

                        	    if tabg[i][j]==tabk[k][l] and tabg[i][j+1]==tabk[k][l+1] and tabg[i][j+2]==tabk[k][l+2] and tabg[i][j+3]==tabk[k][l+3] and tabg[i][j+4]==tabk[k][l+4]:
                                        if tabk[k][6]=='0':
                                    	    tabl[i][j] = tabl[i][j] + waga
                                        elif tabk[k][6]=='1':
                                	    tabl[i][j+1] = tabl[i][j+1] + waga
                                        elif tabk[k][6]=='2':
                                       	    tabl[i][j+2] = tabl[i][j+2] + waga
                                        elif tabk[k][6]=='3':
                                	    tabl[i][j+3] = tabl[i][j+3] + waga
                                        elif tabk[k][6]=='4':
                                            tabl[i][j+4] = tabl[i][j+4] + waga
                                    if tabg[i][j]==tabk[k][l] and tabg[i+1][j+1]==tabk[k][l+1] and tabg[i+2][j+2]==tabk[k][l+2] and tabg[i+3][j+3]==tabk[k][l+3] and tabg[i+4][j+4]==tabk[k][l+4]:	
                                        if tabk[k][6]=='0':
                	                    tabl[i][j] = tabl[i][j] + waga
                                        elif tabk[k][6]=='1':
                                       	    tabl[i+1][j+1] = tabl[i+1][j+1] + waga
                                        elif tabk[k][6]=='2':
                                       	    tabl[i+2][j+2] = tabl[i+2][j+2] + waga
                                        elif tabk[k][6]=='3':
                                	    tabl[i+3][j+3] = tabl[i+3][j+3] + waga
                                        elif tabk[k][6]=='4':
                                	    tabl[i+4][j+4] = tabl[i+4][j+4] + waga
            
                            	    if tabg[i][j]==tabk[k][l] and tabg[i+1][j]==tabk[k][l+1] and tabg[i+2][j]==tabk[k][l+2] and tabg[i+3][j]==tabk[k][l+3] and tabg[i+4][j]==tabk[k][l+4]:
                                        if tabk[k][6]=='0':
                                	    tabl[i][j] = tabl[i][j] + waga
                                        elif tabk[k][6]=='1':
                    	                    tabl[i+1][j] = tabl[i+1][j] + waga
                                        elif tabk[k][6]=='2':
                                	    tabl[i+2][j] = tabl[i+2][j] + waga
                                        elif tabk[k][6]=='3':
                                       	    tabl[i+3][j] = tabl[i+3][j] + waga
                                        elif tabk[k][6]=='4':
                                	    tabl[i+4][j] = tabl[i+4][j] + waga	
    	                            if j>3:
                		        if tabg[i][j]==tabk[k][l] and tabg[i+1][j-1]==tabk[k][l+1] and tabg[i+2][j-2]==tabk[k][l+2] and tabg[i+3][j-3]==tabk[k][l+3] and tabg[i+4][j-4]==tabk[k][l+4]:	
                                	    if tabk[k][6]=='0':
                                                tabl[i][j] = tabl[i][j] + waga
                                	    elif tabk[k][6]=='1':
                                                tabl[i+1][j-1] = tabl[i+1][j-1] + waga
                                	    elif tabk[k][6]=='2':
                                                tabl[i+2][j-2] = tabl[i+2][j-2] + waga
                                	    elif tabk[k][6]=='3':
                                                tabl[i+3][j-3] = tabl[i+3][j-3] + waga
                                	    elif tabk[k][6]=='4':
                                                tabl[i+4][j-4] = tabl[i+4][j-4] + waga    
                        for i in range(liczba_pol):
        	            for j in range(liczba_pol):
                                if tabl[i][j]>tabl[imax][jmax]:
                                    imax = i
                        	    jmax = j
    	                tabg[imax][jmax] = 'O'

                        for i in range(liczba_pol):
                    	    for j in range(liczba_pol):
                                if tabg[i][j]=='O' and tabg[i][j+1]=='O' and tabg[i][j+2]=='O' and tabg[i][j+3]=='O' and tabg[i][j+4]=='O':
                            	    wygrana_komputera = True
                                if tabg[i][j]=='O' and tabg[i+1][j+1]=='O' and tabg[i+2][j+2]=='O' and tabg[i+3][j+3]=='O' and tabg[i+4][j+4]=='O':        
                            	    wygrana_komputera = True
                                if tabg[i][j]=='O' and tabg[i+1][j]=='O' and tabg[i+2][j]=='O' and tabg[i+3][j]=='O' and tabg[i+4][j]=='O':
                            	    wygrana_komputera = True
                                if j>3:
                        	    if tabg[i][j]=='O' and tabg[i+1][j-1]=='O' and tabg[i+2][j-2]=='O' and tabg[i+3][j-3]=='O' and tabg[i+4][j-4]=='O':
                                        wygrana_komputera = True
                    
                        list_ox.append(jmax)
                        list_oy.append(imax)
                        list_ox = ' '.join(map(str, list_ox))
                        list_oy = ' '.join(map(str, list_oy))
                        p = Coord_o(ip = client_ip, coord_ox = list_ox, coord_oy = list_oy)
                        p.save()
                        p.coord_ox
                        print (imax)
                        print (list_ox)
                        print (p.coord_ox)
                        imax = imax + 1
                        jmax = jmax + 1
                        result = imax * 100 + jmax
        if rest_of_modulo_of_number != 0:
            result = "Wybrano poziom"
        if wygrana_gracza == True:
            result = "Gracz wygral"
        elif wygrana_komputera == True:
            result = result *100 



    return render(request, 'game/index.html',{'content':result})



