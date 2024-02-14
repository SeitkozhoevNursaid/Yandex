import sqlite3
import requests



conn = sqlite3.connect('pharma.sqlite3')

api_key = '1e14af53-9da6-4087-8a2d-bb1061e004fd'
search_query = 'аптека'
latitude = 42.87  
longitude = 74.59  
spn = '0.5,0.5'


url = f'https://search-maps.yandex.ru/v1/?apikey={api_key}&text={search_query}&ll={longitude},{latitude}&spn={spn}&results=80&lang=ru_RU'

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS pharmacies
                  (id INTEGER PRIMARY KEY, name TEXT)''')


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for result in data['features']:
        name = result['properties']['name']
        cursor.execute("INSERT INTO pharmacies (name) VALUES (?)", (name,))
        conn.commit()  


cursor.execute("SELECT * FROM pharmacies")
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()
conn.close()




































# import sqlite3;
 
# sqlite3.connect('/home/nursaid/Рабочий стол/informatic/pharmacy.db', timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
 
# con = sqlite3.connect("pharmacy.db")
# cursor = con.cursor()



# cursor.execute("INSERT INTO pharmacies (Field2) VALUES (?)", name )