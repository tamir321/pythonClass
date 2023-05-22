from multiprocessing import Process, Pipe

def f(conn):
    conn.send(['hello', 'world'])
    print("conn.recv() in child ",conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # ['hello', 'world']
    parent_conn.send(['hello', 'back'])
    p.join()
