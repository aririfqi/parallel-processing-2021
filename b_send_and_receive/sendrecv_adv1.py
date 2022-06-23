from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("rank %d " % rank,end=" ")
if rank == 0:
    data1 = 10
    data2 = 200
    comm.send(data1, dest=1, tag=100)
    comm.send(data2, dest=2,tag=100)
    print("mengirim")
    data3 =comm.recv(source=3, tag=102)
    data4 = comm.recv(source=4, tag=103)*5
    dataHasil = data3+data4
    print(dataHasil)
elif rank == 1:
    data5 = comm.recv(source=0,tag=100)
    data5 += 10
    print("Hasil Sementara : %d " % (data5))
    comm.send(data5,dest=3,tag=100)
elif rank == 2:
    data6 = comm.recv(source=0,tag=100)
    data6 -= 10
    comm.send(data6,dest=4,tag=100)
    print("Hasil Sementara : %d " % (data6))
elif rank == 3:
    data7 = comm.recv(source=1,tag=100)
    data7 **= 2
    print("Hasil Akhir : %d " % (data7))
    comm.send(data7,dest=0,tag=102)
elif rank == 4:
    data8 = comm.recv(source=2,tag=100)
    data8 **= 2
    print("Hasil Akhir : %d " % (data8))
    comm.send(data8,dest=0,tag=103)
else:
    print("Tidak Bekerja")