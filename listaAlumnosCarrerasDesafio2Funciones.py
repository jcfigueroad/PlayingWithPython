countCarrera = 0
listaAlumnos = []
listaCarreras = []

def guardar_archivo(nombre_archivo, object):
	fd = open(nombre_archivo,'w')
	fd.write(str(object))
	fd.close()

def guardar_archivo_with(nombre_archivo, object):
	with open(nombre_archivo, 'w') as fd:
		fd.write(str(object))

def guardar_like_json(nombre_archivo, object):
	with open(nombre_archivo, 'w') as fd:
		alumnosJSON = json.dumps(object)
		fd.write(alumnosJSON)


def buscar_alumno():
	nombreAlumno = input("Ingrese el nombre del alumno a buscar: ")
	try:
		indice = listaAlumnos.index(nombreAlumno)
		print(listaCarreras[indice])
	except ValueError:
		print("Alumno no encontrado :(")
		buscar_alumno()

def llenar_listas(numeroAlumnos):
	countAlumnos = 0
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
	guardar_archivo_with("alumnos.txt",listaAlumnos)
	

def listar_alumnos():
	print(listaAlumnos)

def consultar_cantidad_alumnos():
	return len(listaAlumnos)

numeroAlumnos = int(input("Ingrese la cantidad de alumnos a ingresar: "))
llenar_listas(numeroAlumnos)
listar_alumnos()
print(listaCarreras)
print("La cantidad de alumnos es %d" % consultar_cantidad_alumnos())
buscar_alumno()

