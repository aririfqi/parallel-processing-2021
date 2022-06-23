#broadcast_adv.py
from mpimanual import broadcastmanual
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data5 = 15
    data6 = 10
else:
    data5 = 1
    data6 = 0
data5 = broadcastmanual(0,[i for i in range(1,comm.size,2)],data5,1,comm)
print("cetak 4 rank %d memiliki data5 : %d " % (rank,data5),flush=True)
data6 = broadcastmanual(0,[i for i in range(1,comm.size,5)],data6,1,comm)
print("cetak 5 rank %d memiliki data6 : %d " % (rank,data6),flush=True)