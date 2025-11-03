import redis
import conexionRedis as cr

#Se añaden los datos para la prueba

usuario1 = {
   "nombre": "Jorge Baron",
   "email": "jorge.baron@example.com",
   "edad": 38,
   "ciudad": "Spain"
}

usuario2 = {
   "nombre": "Elena Gómez",
   "email": "elena.gomez@example.com",
   "edad": 29,
   "ciudad": "Mexico"
}

usuario3 = {
   "nombre":"Pepe garcia",
   "email": "pepe.garcia@example.com",
   "ciudad": 33,
   "edad": "Spain"
}

user1Set = cr.baseDatosRedis.json().set("usuarios:1", cr.Path.root_path(), usuario1)
user2Set = cr.baseDatosRedis.json().set("usuarios:2", cr.Path.root_path(), usuario2)
user3Set = cr.baseDatosRedis.json().set("usuarios:3", cr.Path.root_path(), usuario3)

resultados = cr.baseDatosRedis.ft("indice:usuarios").search(
   cr.Query("Jorge @edad:[30 40]")
)

groupby = cr.aggregations.AggregateRequest("*").group_by(
   '@ciudad', cr.reducers.count().alias('count')
)

resultado = cr.baseDatosRedis.ft("indice:usuarios").aggregate(groupby).rows
print(resultado)



