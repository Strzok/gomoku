# -*- coding: utf-8 -*-

from django.shortcuts import render
from game.models import Coord_o
from game.models import Coord_x
from game.models import Difficulty_level
from game.models import Size
from django.http import HttpRequest
from django.contrib.postgres.fields import ArrayField

# Create your views here.

def index(request):
    return render(request, 'game/index.html',{})


def result(request, number):
    client_ip = request.META.get("REMOTE_ADDR")#it takes ip
    result = 759

    if number == 'size10' or number == 'size15' or number == 'size20' or number == 'size25' :
        print ("zmiana poziomu")
        number_of_fields = number[4:6]

        c = Size(ip = client_ip, size_in_model = number_of_fields)
        c.save()
        print (number_of_fields)
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
            p = Coord_o(ip = client_ip, coord_ox = '0', coord_oy = '0')#creation of entry
            p.save()

        try:
            g = Difficulty_level.objects.get(ip = client_ip)
        except Difficulty_level.DoesNotExist:
	        h = Difficulty_level(ip = client_ip, level_in_model = '3')
	        h.save()

        try:
            k = Size.objects.get(ip = client_ip)
        except Size.DoesNotExist:
	        l = Size(ip = client_ip, size_in_model = '15')
	        l.save()


    else:
        try:
            Coord_o.objects.get(ip = client_ip)#get o from database for given ip
        except Coord_o.DoesNotExist:
            p = Coord_o(ip = client_ip, coord_ox = '0', coord_oy = '0')#creation of entry
            p.save()

        try:
            Coord_x.objects.get(ip = client_ip)#get x from database for given ip
        except Coord_x.DoesNotExist:
            q = Coord_x(ip = client_ip, coord_xx = '0', coord_xy = '0')
            q.save()

        try:
            Difficulty_level.objects.get(ip = client_ip)
        except Difficulty_level.DoesNotExist:
            h = Difficulty_level(ip = client_ip, level_in_model = '3')
            h.save()

        try:
            Size.objects.get(ip = client_ip)
        except Size.DoesNotExist:
	        l = Size(ip = client_ip, size_in_model = '15')
	        l.save()


        coord_o = Coord_o.objects.get(ip = client_ip)     #extracting a record with data of computer moves
        coord_x = Coord_x.objects.get(ip = client_ip)

        difficulty_level =  Difficulty_level.objects.get(ip = client_ip)
        difficulty_level.save
        level = difficulty_level.level_in_model

        size = Size.objects.get(ip = client_ip)
        size.save
        number_of_fields = size.size_in_model

        coord_o.save
        coord_x.save
        list_ox = []#declaration of lists
        list_oy = []
        list_xx = []
        list_xy = []

        list_ox = coord_o.coord_ox #list of coordinates of computer moves by x
        list_oy = coord_o.coord_oy #list of coordinates of computer moves by y
        list_xx = coord_x.coord_xx
        list_xy = coord_x.coord_xy

        list_ox = list_ox.split(' ')#spliting taken variables from str to list
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
        column = number%100
        horizontal_line = (number-column)/100
        column = int(column)
        horizontal_line = int(horizontal_line)
        column = column-1
        horizontal_line = horizontal_line-1
        number_of_fields = int(number_of_fields)
        tabg = [['-'for col in range(number_of_fields+5)]for row in range(number_of_fields+5)]
        tabg[horizontal_line][column] = 'X'

        for i in range(1,len(list_xy)):#change lists of strings to lists of integers
            list_xy[i] = int(list_xy[i])
            list_xx[i] = int(list_xx[i])

        for i in range(1,len(list_xy)):#fill tabg by Xs where a player gave a cross
        	tabg[list_xy[i]][list_xx[i]] = 'X'

        print (tabg)

        if list_xx:
            list_xx.append(column)#adding coordinates of last player's move to list
            list_xy.append(horizontal_line)
            list_xx = ' '.join(map(str, list_xx))#joining lists to str
            list_xy = ' '.join(map(str, list_xy))
            p = Coord_x(ip = client_ip, coord_xx = list_xx, coord_xy = list_xy)#putting lists to database
            p.save()
            p.coord_xx


        for i in range(1,len(list_oy)):#change lists of strings to lists of integers
            list_oy[i] = int(list_oy[i])
            list_ox[i] = int(list_ox[i])

        for i in range(1,len(list_oy)):#filling tabg by O(computer moves)
        	tabg[list_oy[i]][list_ox[i]] = 'O'

        print (tabg)

        computer_starts = False
        a = False

        if computer_starts == True:
            tabg[number_of_fields/2][number_of_fields/2] = 'O'

        win_of_player = False
        win_of_computer = False
        decision_of_computer = False

        for i in range(number_of_fields):
            for j in range(number_of_fields):
                if tabg[i][j]=='X' and tabg[i][j+1]=='X' and tabg[i][j+2]=='X' and tabg[i][j+3]=='X' and tabg[i][j+4]=='X':
                    win_of_player = True
                if tabg[i][j]=='X' and tabg[i+1][j+1]=='X' and tabg[i+2][j+2]=='X' and tabg[i+3][j+3]=='X' and tabg[i+4][j+4]=='X':
                    win_of_player = True
                if tabg[i][j]=='X' and tabg[i+1][j]=='X' and tabg[i+2][j]=='X' and tabg[i+3][j]=='X' and tabg[i+4][j]=='X':
                    win_of_player = True
                if j>3:
                    if tabg[i][j]=='X' and tabg[i+1][j-1]=='X' and tabg[i+2][j-2]=='X' and tabg[i+3][j-3]=='X' and tabg[i+4][j-4]=='X':
                        win_of_player = True

        if win_of_player == False:
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
            ['-','-','O','-','-','_','1','_','P']
            ]

            wage = 0
            l = 0
            imax = 0 #field coordinate in the highest priority value
            jmax = 0 #field coordinate in the highest priority value


            tabl = [[ 0 for col in range(number_of_fields+5)]for row in range(number_of_fields+5)]
            for i in range(number_of_fields):
                for j in range(number_of_fields):
                    for k in range(54):
                        if tabk[k][8]=='Q':
                            wage = 3750000
                        elif tabk[k][8]=='W':
                            wage = 750000
                        elif tabk[k][8]=='E':
                            wage = 150000
                        elif tabk[k][8]=='R' and level == '4':
                            wage = 30000
                        elif tabk[k][8]=='T' and level == '4':
                            wage = 3000
                        elif tabk[k][8]=='Y' and level == '4':
                            wage = 300
                        elif tabk[k][8]=='U' and level == '4':
                            wage = 30
                        elif tabk[k][8]=='I' and level == '4':
                            wage = 3
                        elif tabk[k][8]=='O' and level == '4':
                            wage = 2
                        elif tabk[k][8]=='U' and level == '3':
                            wage = 1
                        elif tabk[k][8]=='I' and level == '3':
                            wage = 1
                        elif tabk[k][8]=='O' and level == '3':
                            wage = 1
                        elif tabk[k][8]=='Y' and level == '2':
                            wage = 1
                        elif tabk[k][8]=='U' and level == '2':
                            wage = 1
                        elif tabk[k][8]=='I' and level == '2':
                            wage = 1
                        elif tabk[k][8]=='O' and level == '2':
                            wage = 1
       	                elif tabk[k][8]=='E' and level == '1':
                            wage = 1
                        elif tabk[k][8]=='R' and level == '1':
                            wage = 1
                        elif tabk[k][8]=='T' and level == '1':
                            wage = 1
                        elif tabk[k][8]=='Y' and level == '1':
                            wage = 1
                        elif tabk[k][8]=='U' and level == '1':
                            wage = 1
                        elif tabk[k][8]=='I'and level == '1':
                            wage = 2
                        elif tabk[k][8]=='O'and level == '1':
                            wage = 2
               	        elif tabk[k][8]=='P':
                            wage = 1
                        else:
                            wage = 0


                        if tabg[i][j]==tabk[k][l] and tabg[i][j+1]==tabk[k][l+1] and tabg[i][j+2]==tabk[k][l+2] and tabg[i][j+3]==tabk[k][l+3] and tabg[i][j+4]==tabk[k][l+4]:
                            if tabk[k][6]=='0':
                    	        tabl[i][j] = tabl[i][j] + wage
                            elif tabk[k][6]=='1':
                	            tabl[i][j+1] = tabl[i][j+1] + wage
                            elif tabk[k][6]=='2':
                       	        tabl[i][j+2] = tabl[i][j+2] + wage
                            elif tabk[k][6]=='3':
                	            tabl[i][j+3] = tabl[i][j+3] + wage
                            elif tabk[k][6]=='4':
                                tabl[i][j+4] = tabl[i][j+4] + wage

                        if tabg[i][j]==tabk[k][l] and tabg[i+1][j+1]==tabk[k][l+1] and tabg[i+2][j+2]==tabk[k][l+2] and tabg[i+3][j+3]==tabk[k][l+3] and tabg[i+4][j+4]==tabk[k][l+4]:
                            if tabk[k][6]=='0':
	                            tabl[i][j] = tabl[i][j] + wage
                            elif tabk[k][6]=='1':
                       	        tabl[i+1][j+1] = tabl[i+1][j+1] + wage
                            elif tabk[k][6]=='2':
                       	        tabl[i+2][j+2] = tabl[i+2][j+2] + wage
                            elif tabk[k][6]=='3':
                	            tabl[i+3][j+3] = tabl[i+3][j+3] + wage
                            elif tabk[k][6]=='4':
                	            tabl[i+4][j+4] = tabl[i+4][j+4] + wage

                        if tabg[i][j]==tabk[k][l] and tabg[i+1][j]==tabk[k][l+1] and tabg[i+2][j]==tabk[k][l+2] and tabg[i+3][j]==tabk[k][l+3] and tabg[i+4][j]==tabk[k][l+4]:
                            if tabk[k][6]=='0':
                	            tabl[i][j] = tabl[i][j] + wage
                            elif tabk[k][6]=='1':
    	                        tabl[i+1][j] = tabl[i+1][j] + wage
                            elif tabk[k][6]=='2':
                	            tabl[i+2][j] = tabl[i+2][j] + wage
                            elif tabk[k][6]=='3':
                       	        tabl[i+3][j] = tabl[i+3][j] + wage
                            elif tabk[k][6]=='4':
                	            tabl[i+4][j] = tabl[i+4][j] + wage

                        if j>3:
                            if tabg[i][j]==tabk[k][l] and tabg[i+1][j-1]==tabk[k][l+1] and tabg[i+2][j-2]==tabk[k][l+2] and tabg[i+3][j-3]==tabk[k][l+3] and tabg[i+4][j-4]==tabk[k][l+4]:
                                if tabk[k][6]=='0':
                                    tabl[i][j] = tabl[i][j] + wage
                                elif tabk[k][6]=='1':
                                    tabl[i+1][j-1] = tabl[i+1][j-1] + wage
                                elif tabk[k][6]=='2':
                                    tabl[i+2][j-2] = tabl[i+2][j-2] + wage
                                elif tabk[k][6]=='3':
                                    tabl[i+3][j-3] = tabl[i+3][j-3] + wage
                                elif tabk[k][6]=='4':
                                    tabl[i+4][j-4] = tabl[i+4][j-4] + wage

            for i in range(number_of_fields):
                for j in range(number_of_fields):
                    if tabl[i][j]>tabl[imax][jmax]:
                        imax = i
                        jmax = j
            tabg[imax][jmax] = 'O'

            for i in range(number_of_fields):
    	        for j in range(number_of_fields):
                    if tabg[i][j]=='O' and tabg[i][j+1]=='O' and tabg[i][j+2]=='O' and tabg[i][j+3]=='O' and tabg[i][j+4]=='O':
            	        win_of_computer = True
                    if tabg[i][j]=='O' and tabg[i+1][j+1]=='O' and tabg[i+2][j+2]=='O' and tabg[i+3][j+3]=='O' and tabg[i+4][j+4]=='O':
            	        win_of_computer = True
                    if tabg[i][j]=='O' and tabg[i+1][j]=='O' and tabg[i+2][j]=='O' and tabg[i+3][j]=='O' and tabg[i+4][j]=='O':
            	        win_of_computer = True
                    if j>3:
                        if tabg[i][j]=='O' and tabg[i+1][j-1]=='O' and tabg[i+2][j-2]=='O' and tabg[i+3][j-3]=='O' and tabg[i+4][j-4]=='O':
                            win_of_computer = True

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

        if win_of_player == True:
            result = "Gracz wygrał"
        elif win_of_computer == True:
            result = result *100



    return render(request, 'game/index.html',{'content':result})



