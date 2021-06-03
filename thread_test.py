import time
import concurrent.futures


def fetch_single(num: str):
    return num

time_start = time.time()

with concurrent.futures.ThreadPoolExecutor() as tpe:
    results = [tpe.submit(fetch_single, i) for i in range(1000)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

time_end = time.time()
print(f'\nTook {round(time_end - time_start, 2)} seconds')