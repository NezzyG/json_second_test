"""oricum e irelevant, o sa iti scriu aici ce idee am sa faci in continuare
vreau sa te joci cu libraria "requests": vreau sa faci request catre pagina asta https://api.mocki.io/v1/b043df5a
response-ul va fi un json (daca intri pe link vei vedea)
vreau sa imi afisezi toate orasele alfabetic
un tiny exercise pt a te invata si cu request-urile catre pagini
si are legatura cu JSON
si la interviul de la voda am avut de facut un request de genul"""





import json

from pprint import pprint



with open("users.json","w",encoding="utf-8") as f:
    data = json.dumps(steam, indent=4)
    f.write(data)
with open("users.json","r",encoding="utf-8") as f:
    data=json.load(f)
    pprint(data)
with open("users.json","w", encoding="utf-8") as f:
    data=json.dumps(data, indent=4)
    f.write(data)