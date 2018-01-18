#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3
import os


def alta():

	os.system("cls")

	nombre = input("Ingrese Nombre....: ")
	apellido_paterno = input("Ingrese apellido Paterno....: ")
	apellido_materno = input("Ingrese apellido Materno....: ")
	direccion = input("Direccion.....: ")
	telefono = int(input("Telefono......: "))
	codigopostal = int(input("Codigo Postal.....: "))

	objeto = input("Articulo a Empeñar......: ")
	cantidad = float(input("Cantidad de Prestamo....:"))

	totalinteres = cantidad*.20

	Total = cantidad+totalinteres

	print("El interes a pagar es :" + str(totalinteres) )

	print("Total para desempeñar el articulo " + str(Total))

	print("")

	print("El Cliente fue dado de alta correctamente \n ")

	input("Presiona cualquier tecla para continuar.....")



while True:

	os.system("cls")

	print("Menu Principal")
	print("")
	print("N    Cliente Nuevo")
	print("R    Refrendos y/o extensiones")
	print("A    Abonos")
	print("L    Liquidaciones")
	print("X    Salir")

	opcion = input("Elija una Opcion    :")

	if (opcion == "N"):

		alta()

	elif(opcion == "R"):

		#refrendos()
		pass

	elif(opcion == "A"):

		#abonos()
		pass

	elif(opcion == "L"):

		#liquidaciones
		pass

	elif(opcion == "X"):
		break

	else:

		print("\nOpcion Incorrecta..... \n ")
		input("Presiones cualquier tecla para continuar")
		
