import redis
import conexionRedis as cr

#Para eliminar claves-valor de la base de datos:
cr.baseDatosRedis.delete("libro_1")
cr.baseDatosRedis.delete("libro_2")
