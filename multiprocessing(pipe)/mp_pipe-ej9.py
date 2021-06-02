from multiprocessing import Process, Pipe
import os
import sys



def reader(l):
    print("Leyendo, presione Ctrl+D para salir")
    sys.stdin = open(0)
    while True:
        msg = input()
        l.send(msg)


def pipe_reader(q):
    while True:
        msg = q.recv()
        print('Leyendo (pid: %d): %s' % (os.getpid(), msg))



if __name__ == "__main__":
    a, b = Pipe()
    proceso1 = Process(target=reader, args=(a,))
    proceso2 = Process(target=pipe_reader, args=(b,))
    proceso1.start()
    proceso2.start()
    proceso1.join()
    proceso2.kill()
