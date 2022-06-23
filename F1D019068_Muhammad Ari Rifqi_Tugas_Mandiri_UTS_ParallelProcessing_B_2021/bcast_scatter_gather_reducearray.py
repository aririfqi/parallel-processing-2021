from mpi4py import MPI
import random as rd
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data0 = [i for i in range(size)]
data0_1 = [i for i in range(10)]
data1 = None

#send data
if rank == 0:
    comm.send(data0, dest=2, tag=100)
    print("Pengiriman data barang dari rank %d ke rank 2 dengan data : "% (rank), data0, flush = True)
    comm.send(data0, dest=3, tag=101)
    print("Pengiriman data barang dari rank %d ke rank 3 dengan data : "% (rank), data0_1, flush = True)
#recv data
elif rank == 2:
    data1 = comm.recv(source=0,tag=100)
    print("Rank %d menerima data barang dari rank 0 dengan data : "% (rank),data1,flush=True)
    print("Rank 2 melakukan broadcast", flush=True)
elif rank == 3:
    data1 = comm.recv(source=0,tag=101)
    print("Rank %d menerima data barang dari rank 0 dengan data : "% (rank),data1,flush=True)
    print("Rank 3 melakukan broadcast", flush=True)

#broadcast data from root 2
data2 = comm.bcast(data1,root=2)
#broadcast data from root 2 to rank 3 and 4
if (rank>2) and (rank<5):
    print("(bcast from root 2)-> Rank %d data : "% (rank),data2,flush=True)
    
#scatter data
data3 = comm.scatter(data2, root=4)
# scatter data from root 4 to rank 5 and 6
if(rank>4) and (rank<7):
    print("Hasil Scatter 01")
    print("Rank %d dengan data : "% (rank), data3, flush=True)
#scatter data from root 3 to rank 7 and 8    
data3_1 = comm.scatter(data2,root=3)
if(rank>6)and(rank<9):
    print("Hasil Scatter 01")
    print("Rank %d dengan data : "% (rank), data3_1, flush=True)
#gather data3 to rank 9    
data4 = comm.gather(data3,root=9)
if(rank>8)and(rank<10):
    print("Hasil Gather 01")
    print("Rank %d dengan data : "% (rank), data4, flush=True)
#gather data3_1 to rank 10    
data4_1 = comm.gather(data3_1,root=10)
if(rank>9)and(rank<11):
    print("Hasil Gather 01")
    print("Rank %d dengan data : "% (rank), data4_1, flush=True)

#scatter data4 from root 9    
data5 = comm.scatter(data4, root=9)
#scatter data4 from root 6 to rank 11,12,13,and 14
if(rank>10) and (rank<15):
    print("Hasil Scatter 02")
    print("Rank %d dengan data : "% (rank), data5, flush=True)

#scatter data4 from root 10 to rank 15,16,17,18   
data5_1 = comm.scatter(data4_1,root=10)
if(rank>14) and (rank<19):
    print("Hasil Scatter 02")
    print("Rank %d dengan data : "% (rank), data5_1, flush=True)

#gather data5
data6 = comm.gather(data5,root=0)
if rank == 0:
    print("Hasil Gather 02")
    print("Rank %d dengan data : "% (rank), data6, flush=True)
#gather data5_1    
data6_1 = comm.gather(data5_1,root=0)
if rank == 0:
    print("Hasil Gather 02")
    print("Rank %d dengan data : "% (rank), data6_1, flush=True)

#broadcast from root 3
data2 = comm.bcast(data1,root=3)
#broadcast data from root 3 to rank 5 and 7
if (rank==5) and (rank==7):
    print("(bcast from root 3)-> Rank %d data : "% (rank),data2,flush=True)
#broadcast data from root 2 to rank 1
elif (rank == 1):
    print("(bcast from root 3)-> Rank %d data : "% (rank),data2,flush=True)
#(cabang kanan)scatter data from root 1 to rank 9,10
data3 = comm.scatter(data2, root=1)
if(rank>8)and(rank<11):
    print("Hasil Scatter Cabang kanan")
    print("Rank %d dengan data : "% (rank), data3, flush=True)
#gather data3 (cabang kanan)
data3 = comm.gather(data3,root=0)
if rank == 0:
    print("Hasil Cabang kanan")
    print("Rank %d dengan data : "% (rank), data3, flush=True)
#reduce data cabang kiri with reduce-array for data0   
outsum = comm.reduce(data0,op=MPI.SUM,root=0)
outmin = comm.reduce(data0,op=MPI.MIN,root=0)
outmax = comm.reduce(data0,op=MPI.MAX,root=0)
if comm.rank == 0:
    print("file (rank %d) SUM : " % (comm.rank),outsum)
    print("file (rank %d) MIN : " % (comm.rank),outmin)
    print("file (rank %d) MAX : " % (comm.rank),outmax)
#reduce data cabang kanan with allreduce for data0_1
outallreduce = comm.allreduce(data0_1,op=MPI.SUM)
if comm.rank ==0:
    print("(allreduce cabang kanan)-> rank %d menerima data : " % (comm.rank),outallreduce,"data")