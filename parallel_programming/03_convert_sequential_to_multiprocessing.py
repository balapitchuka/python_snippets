import time
import multiprocessing


def calc_square(numbers):
    for number in numbers:
        time.sleep(5)
        print('square ', number*number)

def calc_cube(numbers):
    for number in numbers:
        time.sleep(5)
        print('cube ', number*number*number)


if __name__ == '__main__':
    start = time.time()
    arr = [2, 3, 5, 7, 11]
    process1 = multiprocessing.Process(target=calc_square, args=(arr, ))
    process2 = multiprocessing.Process(target=calc_cube, args=(arr, ))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('executing took: ', time.time() - start)
    print('Done!!')