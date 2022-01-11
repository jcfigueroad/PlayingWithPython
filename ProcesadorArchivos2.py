import json

class ProcesadorArchivos2:
	def __init__(self):
		self.nombre_archivo_alumnos = "procesadorTextoAlumnos.txt"
		self.nombre_archivo_carreras = "procesadorTextoCarreras.txt"
		self.lista_alumnos = []
		self.lista_carreras = []
	def leerDatosArchivoJSON(self,nombre_archivo):
		try:
			with open(nombre_archivo, 'r') as fd:
				datos = json.loads(fd.read())
				print(datos)
		except FileNotFoundError:
			with open(nombre_archivo, 'x') as fd:
				print("Archivo %s vacio" % nombre_archivo)
	def escribirDatosArchivoJSON(self, nombre_archivo, lista):
		with open(nombre_archivo, 'w') as fd:
			fd.write(json.dumps(lista))

pa = ProcesadorArchivos2()
pa.leerDatosArchivoJSON(pa.nombre_archivo_alumnos)
pa.escribirDatosArchivoJSON(pa.nombre_archivo_alumnos, ["pedro", "juan"])
pa.leerDatosArchivoJSON(pa.nombre_archivo_alumnos)
