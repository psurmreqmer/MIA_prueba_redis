import redis
import conexionRedis as cr



# Podemos guardar archivos JSON en nuestra base de datos Redis:
res1 = cr.baseDatosRedis.json().set("usuarios:1", "$", {"nombre": "Jorge", "apellido": "Baron", "edad": 37})
res2 = cr.baseDatosRedis.json().set("usuarios:2", "$", {"nombre": "Lucía", "apellido": "Benitez", "edad": 24})

#O podemos guardar un array de datos en json:
cr.baseDatosRedis.json().set("usuarios_array", "$", [])
res3 = cr.baseDatosRedis.json().arrappend("usuarios_array", "$", {"nombre": "Pepe", "apellido": "Sanchez", "edad": 45})
res4 = cr.baseDatosRedis.json().arrappend("usuarios_array", "$", {"nombre": "Calisto", "apellido": "Melibea", "edad": 67})

