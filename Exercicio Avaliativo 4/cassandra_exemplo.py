from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

auth = {}

with open('atividade4-token.json') as file:
   auth = json.load(file)

   
cloud_config= {
  'secure_connect_bundle': 'secure-connect-atividade4.zip'
}


auth_provider = PlainTextAuthProvider(
   username=auth['clientId'],
   password=auth['secret']
   )
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")