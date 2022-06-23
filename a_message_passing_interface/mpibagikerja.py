from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
data4 = [i for i in range(200)]
i = ceil(len(data4)/comm.size)
j = comm.rank*i
if(j+i)>=len(data4):
    k = len(data4)
else:
    k = j+i
print(comm.rank,"mengerjakan %d %d" % (j,k),
     data4[j:k],len(data4[j:k]), "dari",len(data4))
print("\n")