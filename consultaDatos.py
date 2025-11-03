#Importamos la librería:
import redis
import conexionRedis as cr



#Obtener el valor de la clave "libro_1" pero en binario:
print(cr.baseDatosRedis.get("libro_1"))
#Obtener el valor de la clave "libro_1" pero en String( Al tener la decodificación ya activada no nos haría falta)
print(cr.baseDatosRedis.get("libro_1").decode("utf-8"))
#Obtener el valor de la clave "libro_2" que al tener tiempo de vida estará ya vacía
print(cr.baseDatosRedis.get("libro_2"))