import time
import multiprocessing

result = []
def calc_square(numbers):
    global result
    for number in numbers:
        # time.sleep(5)
        print('square ', number*number)
        result.append(number * number)
    print('result from multiprocess: ', result)



if __name__ == '__main__':
    start = time.time()
    arr = [2, 3, 5, 7, 11]
    process1 = multiprocessing.Process(target=calc_square, args=(arr, ))

    process1.start()
    
    process1.join()

    print('result is : ', result)
    print('executing took: ', time.time() - start)
    print('Done!!')