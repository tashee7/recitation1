import sys


def fizbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Bizz') #bizz
        elif i % 5 == 0:
            print ('Fuzz') #Buzz
        else:
            print (i)


def main(argv):
    n = int(argv[1])
    fizbuzz(n)


if __name__ == "__main__":
    main(sys.argv)