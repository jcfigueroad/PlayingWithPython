numeroAlumnos = int(input("Ingrese la cantidad de alumnos a ingresar: "))
countAlumnos = 0
countCarrera = 0
listaAlumnos = []
listaCarreras = []
while countAlumnos < numeroAlumnos:
	nombreAlumno = input("Ingrese el numbre del alumno n° %d: " %countAlumnos)
	listaAlumnos.append(nombreAlumno)
	countCarrera = 0
	listaCarreras.append([])
	for countCarrera in range(3):
		carrera = input("Ingrese la carrera n° %d para el alumno %s" % (countCarrera,nombreAlumno))
		listaCarreras[countAlumnos].append(carrera)	
	countAlumnos += 1
print(listaAlumnos)
print(listaCarreras)
