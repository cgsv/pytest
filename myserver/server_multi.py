import sys, time, launcelot
from multiprocessing import Process
from server_simple import server_loop
from threading import Thread

WORKER_CLASS = {'thread': Thread, 'process': Process}
WORKER_MAX = 10

def start_worker(Worker, listen_sock):
    worker = Worker(target = server_loop, args=(listen_sock,))
    #worker.daemon = True
    worker.start()
    return worker

if __name__ == '__main__':
    Worker = WORKER_CLASS[sys.argv.pop()]
    listen_sock = launcelot.setup()
    workers = []
    for i in range(WORKER_MAX):
        workers.append(start_worker(Worker, listen_sock))

    while True:
        time.sleep(2)
        for worker in workers:
            if not worker.is_alive():
                print worker.name, "died; restarting"
                workers.remove(worker)
                workers.append(start_worker(Worker, listen_sock))

