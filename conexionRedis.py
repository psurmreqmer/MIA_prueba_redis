#Importamos la librería:
import redis

from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType

from redis.commands.search.query import Query
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers


#Creamos la conexión a Redis:
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

#Si queremos que la conexión decodifique directamente:
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)

#comprueba que se conecta
print(baseDatosRedis.ping())

#squema

''' Esto solo se ejecuta 1 vez
squema = (
   TextField("$.nombre", as_name="nombre"),
   TagField("$.ciudad", as_name="ciudad"),
   NumericField("$.edad", as_name="edad")
)

indexCreated = baseDatosRedis.ft("indice:usuarios").create_index(
   squema,
   definition=IndexDefinition(
       prefix=["usuarios:"], index_type=IndexType.JSON
   )
)
'''


baseDatosRedis.close()