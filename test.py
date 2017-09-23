import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '4c7d898333a84c8f939497f9f1f84ff9', 'X-Response-Control': 'full' }
connection.request('GET', '/v1/competitions', None, headers )
reponse = connection.getresponse()
competitions = json.loads(reponse.read().decode())
headers = reponse.getheaders()
print((headers))

for competition in competitions :
    print(competition['caption'],' | ',competition['lastUpdated'])
    # Dictionnaire de compétition 
    print('----') 

