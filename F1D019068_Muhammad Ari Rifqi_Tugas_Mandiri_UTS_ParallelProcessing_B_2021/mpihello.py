from mpi4py import MPI
comm = MPI.COMM_WORLD
if comm.rank == 0:
    print("Barang Pokok Sekolah")
elif comm.rank == 4:
    print("Barang Penunjang Sekolah")
else:
    print("Barang reguler no ", comm.rank, " dari total keseluruhan barang : ", comm.size)