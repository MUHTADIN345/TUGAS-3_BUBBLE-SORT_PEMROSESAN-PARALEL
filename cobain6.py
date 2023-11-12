from mpi4py import MPI
import numpy as np

def parallel_bubble_sort(data, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()

    local_data = np.array_split(data, size)[rank]

    n = len(local_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if local_data[j] > local_data[j + 1]:
                local_data[j], local_data[j + 1] = local_data[j + 1], local_data[j]

    sorted_data = comm.gather(local_data, root=0)

    if rank == 0:
        merged_data = np.concatenate(sorted_data)
        merged_data.sort()
        return merged_data
    else:
        return None

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        try:
            num_elements = int(input("Masukkan jumlah elemen dalam array: "))
            data = []
            for i in range(num_elements):
                element = int(input(f"Masukkan elemen array bilangan {i + 1}: "))
                data.append(element)
        except ValueError:
            print("Input harus berupa angka.")
            exit(1)
    else:
        data = None

    data = comm.bcast(data, root=0)

    sorted_data = parallel_bubble_sort(data, comm)

    if rank == 0:
        print("Array yang diurutkan:", sorted_data)
