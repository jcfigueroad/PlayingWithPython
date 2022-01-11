#!/usr/bin/python33


import random
import time
from prettytable import PrettyTable

ranking = {}
pivot_number = 0

def menu():
	print("Menu")
	print("[1] Jugar")
	print("[2] Ver ranking")
	print("[3] Salir")
	opcion = int(input("Ingrese su opción: "))
	return opcion

def consult_number(number,pivot_number):
	if number == pivot_number:
		return 0
	else:
		if number > pivot_number:
			return 1
		else:
			return -1

def main():
	while True:
		pivot_number = random.randint(1,101)
		print("pivot_number: %d " % pivot_number)
		opcion = menu()
		if opcion == 1:
			nombre_jugador = input("Ingresa tu nombre: ")
			init_stamp = time.time()
			while True:
				number = int(input("Ingresa el numero incognito: "))
				if number == -1: 
					break

				result = consult_number(number,pivot_number)
				if result == 0:
					elapsed_time = time.time() - init_stamp
					ranking[nombre_jugador] = elapsed_time
					print("Felicitaciones encontraste el número")
					break
				if result == 1:
					print("Tu número es mayor al número incognito")
				if result == -1:
					print("Tu número es menor al número incognito")
					
		if opcion == 2:
			x = PrettyTable()
			x.field_names = ["Gamer", "Time"]
			x.align["Gamer"] = "l"
			x.align["Time"] = "l"
			ranking_sorted = sorted(ranking.items(), key = lambda x : x[1])
			for item in ranking_sorted:				
				x.add_row([item[0],round(item[1],2)])
			print(x)
		if opcion == 3:
			break

main()
