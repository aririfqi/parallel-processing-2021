from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = [rank,20*rank,20]
data = comm.gather(data, root=0)
if rank == 0:
    print("[rank, 20*rank, jumlahbarang]")
    print(type(data))
    print(data)