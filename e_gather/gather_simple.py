from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = [rank,45*rank,45]
data = comm.gather(data, root=0)
if rank == 0:
    print(type(data))
    print(data)