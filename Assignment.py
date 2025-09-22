import sys
import numpy as np

def main():
    a = np.array([[10,20],[30,40]])
    b = np.array([[50,60],[70,80]])
    print("array a:")
    print(a)
    print("array b:")
    print(b)

    c = a + b
    print("array c:")
    print(c)

    d = a * b
    print ("array d:")
    print(d)

    e = a @ b
    print("array e:")
    print(e)


    return 0
if __name__ == '__main__':
    sys.exit(main())
