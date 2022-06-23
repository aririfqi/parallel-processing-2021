from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data1 = 10
out = comm.allreduce(data1,op=MPI.SUM)
print("rank %d menerima data : " % (comm.rank),out,"data")