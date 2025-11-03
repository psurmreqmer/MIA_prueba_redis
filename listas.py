import redis
import conexionRedis as cr

#Podemos tener listas en redis también:
#Añadimos a la lista:
cr.baseDatosRedis.lpush("usuarios:hobbies", "futbol:1") 
cr.baseDatosRedis.lpush("usuarios:hobbies", "tenis:2")
cr.baseDatosRedis.lpush("usuarios:hobbies", "rugby:2") 
#Obtener todos los elementos:
print(cr.baseDatosRedis.lrange("usuarios:hobbies",0,-1))
#Obtener el primer elemento y eliminarlo:
cr.baseDatosRedis.rpop("usuarios:hobbies")
