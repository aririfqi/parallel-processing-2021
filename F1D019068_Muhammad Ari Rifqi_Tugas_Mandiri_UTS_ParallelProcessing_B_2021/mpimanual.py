#mpimanual.py
def broadcastmanual(source,dest,data,tag,comm):
    if comm.rank == source:
        for x in dest:
            comm.send(data,dest=x,tag=tag)
        return data
    elif comm.rank in dest:
        return comm.recv(source=source,tag=tag)
    else:
        return data