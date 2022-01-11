countAlumnos = 0
countCarrera = 0
listaAlumnos = []
listaCarreras = []

def buscar_en_lista():
	nombreAlumno = input("Ingrese el nombre del alumno a buscar: ")
	try:
		indice = listaAlumnos.index(nombreAlumno)
		print(listaCarreras[indice])
	except ValueError:
		print("Alumno no encontrado :(")
		buscar_en_lista()

numeroAlumnos = int(input("Ingrese la cantidad de alumnos a ingresar: "))
while countAlumnos < numeroAlumnos:
	nombreAlumno = input("Ingrese el numbre del alumno n° %d: " %countAlumnos)
	listaAlumnos.append(nombreAlumno)
	countCarrera = 0
	listaCarreras.append([])
	countCarreras = 0
	while countCarrera < 3:
		carrera = input("Ingrese la carrera n° %d para el alumno %s: " % (countCarrera,nombreAlumno))
		if carrera not in listaCarreras[countAlumnos]:
			listaCarreras[countAlumnos].append(carrera)
			countCarrera += 1	
	countAlumnos += 1
print(listaAlumnos)
print(listaCarreras)

buscar_en_lista()

