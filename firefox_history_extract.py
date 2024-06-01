import os

import sqlite3



# Veri yolunu oluşturma

data_path = os.path.expanduser('~') + "/.mozilla/firefox/kcsu7yo4.default-esr"

history_db = os.path.join(data_path, 'places.sqlite')



# sqlite3 veritabanı ile bağlantı kurma

c = sqlite3.connect(history_db)



# Sorguyu yürütmek için imleç nesnesi oluşturma

cursor = c.cursor()

select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"

cursor.execute(select_statement)



# Sonucu getir ve sonucu yazdır

results = cursor.fetchall()



for url, count in results:

    print(url)



# İmleci kapat

cursor.close()

