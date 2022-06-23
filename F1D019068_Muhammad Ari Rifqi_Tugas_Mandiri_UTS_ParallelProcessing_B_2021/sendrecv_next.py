from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("File (rank) %d " % rank,end=" ")
if rank == 0:
    c = 10
    comm.send(c, dest=1, tag = 100)
    comm.send([2,3,4], dest=1,tag=101)
    comm.send(c,dest=2, tag=103)
    print("mengirim data barang")
elif rank == 1:
    d = comm.recv(source=0,tag=101)
    c = comm.recv(source=0,tag=100)
    print("menerima  c: %d barang kebutuhan sekolah\n\t\t\t d: %s" % (c,d), "(nomor barang tertentu)")
elif rank == 2:
    c = comm.recv(source=0,tag=103)
    print("menerima c: %d " % (c),"barang kebutuhan sekolah")
else:
    print("Tidak merekap")