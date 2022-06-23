#broadcast.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data1 = 10
    data2 = 20
elif rank == 2:
    data1 = 15
    data2 = 5
else:
    data1 = 0
    data2 = 0
print("cetak 1 rank %d memiliki jumlah data1 : %d " % (rank,data1),flush=True)
print("cetak 1 rank %d memiliki jumlah data2 : %d " % (rank,data2),flush=True)
data1 = comm.bcast(data1,root=0)
data2 = comm.bcast(data2,root=2)

print("cetak 2 rank %d memiliki jumlah data1 : %d " % (rank,data1),flush=True)
print("cetak 2 rank %d memiliki jumlah data2 : %d " % (rank,data2),flush=True)