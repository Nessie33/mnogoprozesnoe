import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1,5)]

    start = time.time()
    for filename in filenames:
        read_info(filename)
    vremya = time.time() - start
    print(f'{vremya} (линейный)')

    start = time.time()
    with multiprocessing.Pool() as pr:
        pr.map(read_info, filenames)
    vremya2 = time.time() - start
    print(f'{vremya2} (многопроцессный)')