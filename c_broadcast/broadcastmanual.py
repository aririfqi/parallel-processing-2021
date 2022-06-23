#broadcastmanual.py
from mpi4py import MPI
def broadcastmanual(source,dest,data,tag,comm):
    if comm.rank == source:
        for x in dest:
            comm.send(data,dest=x,tag=tag)
        return data
    elif comm.rank in dest:
        return comm.recv(source=source,tag=tag)
    else:
        return data


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data1 = 45
else:
    data1 = 0
print("cetak 1 rank %d memiliki data1 : %d " % (rank,data1),flush=True)
comm.barrier()
data1 = broadcastmanual(0,[2,3,4],data1,1,comm)
print("cetak 2 rank %d memiliki data1 : %d " % (rank,data1),flush=True)