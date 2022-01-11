import re
from collections import Counter
datos_archivo = None

with open('sesion_03_actividades_access.log','r') as archivo_log:
	datos_archivo = archivo_log.readlines()
	#regularExpresion = r'(2[0-5][0-5]|1\d\d|\d\d|\d)(\.(2[0-5][0-5]|1\d\d|\d\d|\d)){3}'
	regular_expresion_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
	regular_expresion_fecha = r'\d{1,2}\/[a-zA-Z]{3}\/\d{4}'
	regular_expresion_method = r'POST|GET|DELETE|PUT|HEAD|OPTIONS|PATCH'
	regular_expresion_data = r'\"\"'
	for linea in datos_archivo:
		print(linea)
		resultado_ip = re.search(regular_expresion_ip, linea)
		resultado_fecha = re.search(regular_expresion_fecha, linea)
		resultado_method = re.search(regular_expresion_method, linea)
		resultado_data = re.search(regular_expresion_data, linea)
		print("IP: %s" % resultado_ip.group(0))
		print("FECHA: %s" % resultado_fecha.group(0))
		print("METHOD: %s" % resultado_method.group(0))
		print("DATA: %s" % resultado_data.group(3))
