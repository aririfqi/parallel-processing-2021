from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("File(rank) %d " % rank,end = " ")
if rank == 0:
    comm.send(45, dest=1, tag = 100)
    comm.send("barang pokok sekolah", dest=2,tag=101)
    print("mengirim barang")
elif rank == 1:
    d = comm.recv(source=0, tag=100)
    print("menerima : %d " % (d), " barang reguler")
elif rank == 2:
    d = comm.recv(source=0,tag=101)
    print("menerima : %s " % (d))
else:
    print("Tidak merekap")