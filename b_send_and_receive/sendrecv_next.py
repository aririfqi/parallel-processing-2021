from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("rank %d " % rank,end=" ")
if rank == 0:
    c = 45
    comm.send(c, dest=1, tag = 100)
    comm.send([2,3,4], dest=1,tag=101)
    comm.send(c,dest=2, tag=103)
    print("mengirim barang")
elif rank == 1:
    d = comm.recv(source=0,tag=101)
    c = comm.recv(source=0,tag=100)
    print("menerima c: %d d: %s" % (c,d))
elif rank == 2:
    c = comm.recv(source=0,tag=103)
    print("menerima c: %d " % (c))
else:
    print("Tidak bekerja")