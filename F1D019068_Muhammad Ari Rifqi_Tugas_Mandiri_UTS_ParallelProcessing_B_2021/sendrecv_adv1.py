from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("File (rank) %d " % rank,end=" ")
if rank == 0:
    data1 = 10
    data2 = 20
    comm.send(data1, dest=1, tag=100)
    comm.send(data2, dest=2,tag=101)
    print("mengirim rincian data barang")
    data3 =comm.recv(source=3, tag=102)
    data4 = comm.recv(source=4, tag=103)*6
    dataHasil = data3+data4
    print("Hasil sendrecv total = ",dataHasil)
elif rank == 1:
    data1 = comm.recv(source=0,tag=100)
    data1 *= 1000000
    print("Hasil Sementara : %d " % (data1))
    comm.send(data1,dest=3,tag=100)
elif rank == 2:
    data2 = comm.recv(source=0,tag=101)
    data2 *= 100000
    comm.send(data2,dest=4,tag=104)
    print("Hasil Sementara : %d " % (data2))
elif rank == 3:
    data3 = comm.recv(source=1,tag=100)
    data3 *= 6
    print("Hasil Akhir : %d " % (data3))
    comm.send(data3,dest=0,tag=102)
elif rank == 4:
    data4 = comm.recv(source=2,tag=104)
    data4 *= 6
    print("Hasil Akhir : %d " % (data4))
    comm.send(data4,dest=0,tag=103)
else:
    print("Tidak Merekap")