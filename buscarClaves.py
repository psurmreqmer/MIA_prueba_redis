import redis
import conexionRedis as cr

#Ahora utilizamos la función scan_iter, que recibe por parámetro un patrón en las claves para obtener sólo las que necesitamos:
cr.baseDatosRedis.set("libro_1","Quijote")
cr.baseDatosRedis.set("libro_2","Hamlet")
cr.baseDatosRedis.set("libro_3","Otelo")
cr.baseDatosRedis.set("comic_1","Mortadelo y Filemón")
cr.baseDatosRedis.set("comic_2","Superman")

print("Los Libros:")
for clave in cr.baseDatosRedis.scan_iter('libro*'):
   print(clave)
  
print("Los Comics:")   
for clave in cr.baseDatosRedis.scan_iter('comic*'):
   print(clave)

'''
El patrón puede ir acompañado por:
*  -> Cualquier número de caracteres o ninguno
?  -> Un Carácter
[]  -> Que contenga los caracteres dentro de los corchetes

'''

