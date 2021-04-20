from os import getpid, fork, wait

def print_times_child():
    for i in range(5):
        print(f'Soy el hijo, PID: {getpid()}')

child = fork()
if child:
    id_process = getpid()
    print(f'Soy el padre, PID: {id_process}, mi hijo es: {child}')
    print(f'Soy el padre, PID: {id_process}, mi hijo es: {child}')
    wait()
    print(f'Mi proceso hijo, PID: {child} termino')
else:
    print_times_child()
    print(f'Hijo PID: {getpid()}, terminando...\n')