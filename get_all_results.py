import requests as req
import json
import sys
import multiprocessing as mp


start = int(sys.argv[1])
stop = int(sys.argv[2])
jobs = int(sys.argv[3])


folder = "tdk_results"

def fetch(n):
    result = req.get("https://sozluk.gov.tr/gts_id?id=" + str(n)).json()
    result = json.dumps(result, ensure_ascii=False)

    with open(folder + "/" + str(n) + ".txt", 'w') as f:
        f.write(result)
        f.write("\n")

with mp.Pool(jobs) as p:
    p.map(fetch, range(start, stop))

print("Done.")


