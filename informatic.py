import sqlite3
import requests



conn = sqlite3.connect('pharma.sqlite3')

api_key = '1e14af53-9da6-4087-8a2d-bb1061e004fd'
search_query = 'аптека'
latitude = 42.87  
longitude = 74.59  
spn = '0.5,0.5'


url = f'https://search-maps.yandex.ru/v1/?apikey={api_key}&text={search_query}&ll={longitude},{latitude}&spn={spn}&results=8&lang=ru_RU'

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS pharmacies
                  (id INTEGER PRIMARY KEY, name TEXT)''')

new_name = set()
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for result in data['features']:
        name = result['properties']['name']
        if name  not in new_name:
            new_name.add(name)
            cursor.execute("INSERT INTO pharmacies (name) VALUES (?)", (name,))
            conn.commit()  
            

cursor.execute("SELECT * FROM pharmacies")
rows = cursor.fetchall()
for row in rows:
    print(row)
    

    


cursor.close()
conn.close()










# with open("new.csv",mode = "w") as new:
#             new.write(new_name)
























