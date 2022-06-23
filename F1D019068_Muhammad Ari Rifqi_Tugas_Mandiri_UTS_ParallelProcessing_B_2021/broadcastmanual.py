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
    data3 = 20
    data4 = 10
else:
    data3 = 0
    data4 = 5
print("cetak 1 rank %d memiliki jumlah data3 : %d " % (rank,data3),flush=True)
comm.barrier()
data3 = broadcastmanual(0,[2,3,4],data3,1,comm)
print("cetak 2 rank %d memiliki jumlah data3 : %d " % (rank,data3),flush=True)
comm.barrier()
data4 = broadcastmanual(0,[2,3,4],data4,1,comm)
print("cetak 3 rank %d memiliki jumlah data4 : %d " % (rank,data4),flush=True)