class ProcesadorArchivos:
	def __init__(self):
		self.nombre_archivo = "procesadorTexto.txt"
		self.lista = []
	def leerDatosArchivo(self):
		try:
			with open(self.nombre_archivo, 'r') as fd:
				datos = fd.read()
				print(datos)
		except FileNotFoundError:
			with open(self.nombre_archivo, 'x') as fd:
				print("Archivo %s vacio" % self.nombre_archivo)
	def escribirDatosArchivo(self, datos):
		self.lista.append(datos)
		with open(self.nombre_archivo, 'w') as fd:
			fd.write(str(self.lista))

pa = ProcesadorArchivos()
pa.leerDatosArchivo()
pa.escribirDatosArchivo("pedro")
pa.escribirDatosArchivo("juan")
pa.leerDatosArchivo()
