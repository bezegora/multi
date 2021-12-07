from hashlib import md5
from random import choice
import concurrent.futures
import time


def generate_coin(c):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            c = f"{s} {h}"
            break
    return c


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for coin in zip(executor.map(generate_coin, [0, 0, 0, 0])):
            print(coin)


if __name__ == '__main__':
    time1 = time.time()
    main()
    print(time.time() - time1)
