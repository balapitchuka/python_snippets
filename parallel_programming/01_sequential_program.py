import time


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
calc_square(arr)
calc_cube(arr)

print('executing took : ', time.time() - start)
print('-- Done!')

