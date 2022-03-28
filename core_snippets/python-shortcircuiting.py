


def true_func(parameter):
    print("Running true func : ", parameter)
    return True

def flase_func(parameter):
    print("Running false func : ", parameter)
    return False

print((flase_func(1) and flase_func(2) or flase_func(3)) and (flase_func(4) or true_func(5) or flase_func(6)))