import redis
import conexionRedis as cr

#Para obtener todas las claves de una base de datos redis:
claves = cr.baseDatosRedis.keys()
#Si queremos mostrar la información de todas las claves:
for clave in claves:
	print('Clave:', clave , ' y Valor: ', cr.baseDatosRedis.get(clave))

