#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def lotek ():
    liczba=random.randint(1,10)
    print('Wylosowałem liczbę od 0-10, masz 3 próby by ją zgadnąć.')


    for i in range(3):

        odp = input('Jaką liczbę od 1 do 10 mam na myśli?  ' )

        if liczba == int(odp):
            print('Wygrałeś')
            break

        elif i == 2 and liczba != int(odp):
             print('Nie zgadłeś, ta liczba to: ' + str (liczba))
            

        else: 
            print('Nie zgadłeś, spróbuj jeszcze raz.')
            print('Próba nr ' + str(i+1))


    ans = input('Czy chcesz zagrać jeszcze raz? wybierz T lub N ')
    if ans == 'T':
         lotek()
    else:
         print ('Nie to nie :) ')



lotek()


            

          

            
   
