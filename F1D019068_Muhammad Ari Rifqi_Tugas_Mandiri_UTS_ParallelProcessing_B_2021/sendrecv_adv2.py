from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

print("File(rank) %d " % rank,end=" ")
if rank == 0:
    data1 = 20
    data2 = 15
    print("mengirim data barang ke ", end=" ")
    for a in range(1,size):
        if a%2==0:
            comm.send(data1,dest=a,tag=100)
            print(a,end="  ")
        else:
            comm.send(data2,dest=a,tag=100)
            print(a,end="  ")
    print()
elif (rank%2)==0:
    data3 = comm.recv(source=0,tag=100)
    print(" : ", end=" | ")
    for a in range(1,size):
        if a%2 !=0:
            comm.send(data3*rank,dest=a,tag=100)
            print("send ", a,data3*rank,end=" | ")
            data5 = comm.recv(source=a,tag=100)
            print("recv ", a,data5*rank,end=" | ")
    print()
else:
    data4 = comm.recv(source=0,tag=100)
    print(" : ",end=" ")
    for a in range(1,size):
        if a%2==0:
            comm.send(data4*rank,dest=a,tag=100)
            print("send ",a,data4*rank,end=" | ")
            data6 = comm.recv(source=a,tag=100)
            print("recv ",a,data6*rank,end=" | ")
    print()