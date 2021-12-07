import concurrent.futures
import urllib
import urllib.request
import time

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


links = open('res.txt', encoding='utf8').read().split('\n')
time1 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(url, exc)
        else:
            print(200)
print(time.time() - time1)
