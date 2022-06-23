from mpi4py import MPI
import random as rd
comm = MPI.COMM_WORLD

data = comm.rank+1
data2 = [comm.rank,data*rd.randint(0,comm.size)]
outsum = comm.reduce(data,op=MPI.SUM,root=0)
outmin = comm.reduce(data,op=MPI.MIN,root=0)
outmax = comm.reduce(data,op=MPI.MAX,root=0)
outprod = comm.reduce(data,op=MPI.PROD,root=0)
outmaxloc = comm.reduce(data2,op=MPI.MAXLOC,root=0)
outminloc = comm.reduce(data2,op=MPI.MINLOC,root=0)
if comm.rank == 0:
    print("Jumlah keseluruhan pengiriman data (rank %d) SUM : " % (comm.rank),outsum)
    print("Nilai Rata-rata Jumlah perekapan data (rank %d) MEAN : " % (comm.rank),outsum/comm.size)
    print("Nilai MIN keseluruhan pengiriman data (rank %d) MIN : " % (comm.rank),outmin)
    print("Nilai MAX keseluruhan pengiriman data (rank %d) MAX : " % (comm.rank),outmax)
    print("Nilai perkalian keseluruhan data rank %d PROD : " % (comm.rank),outprod)
    print("Nilai pengiriman data terbesar dan rank-nya %d MAXLOC : " % (comm.rank),outmaxloc)
    print("Nilai pengiriman data terkecil dan rank-nya %d MINLOC : " % (comm.rank),outminloc)