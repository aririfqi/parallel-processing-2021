from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data1 = 10
data2 = "test 123"
data3 = [i for i in range(size)]
data4 = [i for i in range(200)]