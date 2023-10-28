from multiprocessing import parent_process, current_process, Process

def task():
    current = current_process()
    parent = parent_process()
    print(f'[{current.name}] esperando a [{parent.name}]...', flush=True)
    parent.join()
    
if __name__ == '__main__':
    current = current_process()
    child = Process(target=task)
    child.start()
    print(f'[{current.name}] esperando a [{child.name}]...', flush=True)
    child.join()
    