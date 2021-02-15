# -*- coding: utf-8 -*-


from DriverInterface import DriverInterface
import logging
from FiscalPrinterDriver import PrinterException


import requests
import json


class FiscalberryDriver(DriverInterface):

	__name__ = "FiscalberryDriver"


	fiscalStatusErrors = []

	printerStatusErrors = []


	def __init__(self, host, port=12000, uri = "http", user = None, password = None, after_port = "api"):
		logging.getLogger().info("conexion con JSON Driver en uri: %s, host: %s puerto: %s" % (uri, host, port))
		self.host = host
		self.port = port
		self.uri = uri
		self.user = user
		self.password = password
		self.after_port = after_port
		self.url = "%s://%s:%s/%s" % (uri, host, port, after_port)

	def start(self):
		"""Inicia recurso de conexion con impresora"""
		pass

	def close(self):
		"""Cierra recurso de conexion con impresora"""
		pass

	def sendCommand(self, jsonData, parameters = None, skipStatusErrors = None):
		"""Envia comando a impresora"""
		url = self.url

		logging.getLogger().info("conectando a la URL %s"%url)
		print jsonData
		headers = {'Content-type': 'application/json'}


		try: 
			if self.password:
				reply = requests.post(url, data=json.dumps(jsonData), headers=headers, auth=(self.user, self.password))
			else:
				reply = requests.post(url, data=json.dumps(jsonData), headers=headers)
			print("INICIANDO::::")
			print reply
			print reply.content
			print("salio la respuesta")
			print(reply.content)
			
			return reply.content
			
		except requests.exceptions.Timeout:			
		    # Maybe set up for a retry, or continue in a retry loop
		    logging.getLogger().error("timeout de conexion con la impresora fiscal")
		except requests.exceptions.RequestException as e:
		    # catastrophic error. bail.
		    logging.getLogger().error(str(e))
		
		

   
