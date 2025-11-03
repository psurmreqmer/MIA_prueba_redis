import redis
import conexionRedis as cr

#En este caso para filtrar en JSON, usaremos la segunda forma para guardarlos, la de array:
res1 = cr.baseDatosRedis.json().get("usuarios_array", '$[?(@.edad > 50)]')
res2 = cr.baseDatosRedis.json().get("usuarios_array", '$[?(@.nombre == "Pepe")]')

print(res1)
print(res2)