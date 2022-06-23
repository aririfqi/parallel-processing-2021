from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

sendbuf = np.zeros(10,dtype='i')+rank
recvbuf = None
if rank == 0:
    recvbuf = np.empty([size, 10], dtype='i')
comm.Gather(sendbuf, recvbuf, root=0)

print("rank %d mengirim %s" % (rank,sendbuf))
print("rank %d menerima %s" % (rank,recvbuf))
