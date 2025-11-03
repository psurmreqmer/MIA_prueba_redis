#Importamos la librería:
import redis

#Creamos la conexión a Redis:
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

#Si queremos que la conexión decodifique directamente:
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)

#comprueba que se conecta
print(baseDatosRedis.ping())

baseDatosRedis.close()