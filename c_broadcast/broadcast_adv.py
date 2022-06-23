#broadcast_adv.py
from mpimanual import broadcastmanual
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data1 = 45
else:
    data1 = 0
data1 = broadcastmanual(0,[i for i in range(1,comm.size,2)],data1,1,comm)
print("rank %d memiliki data1 : %d " % (rank,data1),flush=True)