import re
from collections import Counter
datos_archivo = None

with open('sesion_03_actividades_access.log','r') as archivo_log:
	datos_archivo = archivo_log.read()
	#regularExpresion = r'(2[0-5][0-5]|1\d\d|\d\d|\d)(\.(2[0-5][0-5]|1\d\d|\d\d|\d)){3}'
	regularExpresion = r'\d{3}\.\d{3}.\d{3}\.\d{3}'
	lista = re.findall(regularExpresion,datos_archivo)
	cuenta = Counter(lista)
	lista = list(cuenta.items())
	lista.sort(key = lambda x: x[1])
	for ip, llamadas in lista:
		print("IP: %s Cuenta: %s" % (ip, llamadas))
