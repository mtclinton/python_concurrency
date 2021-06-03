from concurrent.futures import ThreadPoolExecutor as Executor

def worker(data):
    # process data
    with Executor(max_workers=10) as exe:
        future = exe.submit(worker, data)