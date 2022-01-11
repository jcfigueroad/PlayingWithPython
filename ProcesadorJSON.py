import urllib3
import json
from prettytable import PrettyTable

class ProcesadorJSONURL:

	def __init__(self):
		self.url='http://arrau.chillan.ubiobio.cl:8075/ubbiot/web/mediciones/medicionespordia/heLMaOHTNY/E1yGxKAcrg/26092019'
	def processJSON(self):
		http = urllib3.PoolManager()
		r = http.request('GET', self.url)
		data = json.loads(r.data.decode('utf-8'))
		#print(data)
		#print(data['data'][0]['valor'])
		x = PrettyTable()
		x.field_names = ["Fecha","Hora","Valor"]
		for item in data['data']:	
			x.add_row([item['fecha'],item['hora'],item['valor']])
		print(x)

procesor = ProcesadorJSONURL()
procesor.processJSON()
