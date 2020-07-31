import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(method.__name__ , "took",(te - ts) * 1000,"ms")
        return result
    return timed