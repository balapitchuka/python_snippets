import time
import threading


def calc_square(numbers):
    print('calculating square of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('square', n*n)

def calc_cube(numbers):
    print('calculating cube of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('cube', n*n*n)

arr = [2, 3, 5, 7, 11]
start = time.time()
thread1 = threading.Thread(target=calc_square, args=(arr, ))
thread2 = threading.Thread(target=calc_cube, args=(arr, ))
thread1.start()
thread2.start()

thread1.join()   # wait till thread1 is done
thread2.join()   # wait till thread2 is done


print('executing took : ', time.time() - start)
print('-- Done!')

