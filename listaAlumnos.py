numeroAlumnos = int(input("Ingrese la cantidad de alumnos a ingresar: "))
count = 0
lista = []
while count < numeroAlumnos:
	nombreAlumno = input("Ingrese el numbre del alumno n° %d: " %count)
	lista.append(nombreAlumno)
	count += 1
print(lista)
