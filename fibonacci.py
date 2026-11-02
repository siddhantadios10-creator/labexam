def nthFibonacci(n):
    if n<=1:
        return n
    else:
        return nthFibonacci(n-1)+nthFibonacci(n-2)
if __name__=='__main__':
    n=4
    print(nthFibonacci(n))
       