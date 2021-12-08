def factor_sum(n):
    fsum = 0
    for i in range(1,n):
        if n % i == 0:
            fsum += i
    return fsum

if __name__ == "__main__":
    sum_amicable = 0
    for n in range(1,10000):
        if factor_sum(factor_sum(n)) == n:
            if n != factor_sum(n):
                print("{} is amicable with {}".format(n, factor_sum(n)))
                sum_amicable += n
    print(sum_amicable)

