from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

#1- Média de gasto total:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
])

writeAJson(result, "Média de gasto total")

#2- Cliente que mais comprou em cada dia:
result = db.collection.aggregate([
     {"$unwind": "$produtos"},
     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
     {"$sort": {"_id.data": 1, "total": -1}},
     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])

writeAJson(result, "Cliente que mais comprou em cada dia")

# 3- Produto mais vendido:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result, "Produto mais vendido")

#4 total de vendas por dia
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": {"data": "$data_compra"}, "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"_id.data": 1}}
])

writeAJson(result, "Total de vendas por dia")

#Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$match": {"produtos.quantidade": {"$gt": 1}}},
    {"$group": {"_id": "$produtos.descricao"}}
])

writeAJson(result, "Produtos com quantidade vendida acima de 1 unidade")




