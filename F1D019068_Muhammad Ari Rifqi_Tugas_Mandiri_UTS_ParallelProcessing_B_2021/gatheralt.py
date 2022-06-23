from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = 78
elif rank == 1:
    data = "barang keperluan sekolah"
elif rank == 2:
    data = [13,16,14,6,15]
elif rank == 3:
    data = True
data = (rank+1)
data = comm.gather(data, root=0)
print("file %d mendapatkan (menerima) data dari rank : %s " % (rank,data))
