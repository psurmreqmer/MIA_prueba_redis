#Importamos la librería:
import redis
import conexionRedis as cr

#Para crar registros en la base de datos sólo debemos lanzar el comando set:
cr.baseDatosRedis.set('libro_1', 'Quijote')
#ex indica que expira a los 10 segundos
cr.baseDatosRedis.set('libro_2', 'Hamlet', ex=10)


cr.baseDatosRedis.close()
