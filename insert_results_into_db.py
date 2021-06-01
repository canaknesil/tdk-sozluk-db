import json
import sys
import sqlite3 as sql


def get_result(n):
    with open("tdk_results/" + str(n) + ".txt") as f:
        js_str = f.read()
    js = json.loads(js_str)
    return js

def insert_js_to_db(c, js):
    assert(len(js) == 1)
    madde = js[0]['madde']
    madde_id = int(js[0]['madde_id'])
    js_str = json.dumps(js, ensure_ascii=False)
    c.execute('insert into results values (?,?,?)', (madde_id, madde, js_str))



all_results = map(get_result, range(100000))
all_results = filter(lambda item: isinstance(item, list), all_results)

conn = sql.connect("tdk_results.db")
c = conn.cursor()
list(map(lambda item: insert_js_to_db(c, item), all_results))
conn.commit()
conn.close()


