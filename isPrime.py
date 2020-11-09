def countPrimes(n):
    isPrim = [True]*n
    # 将数组都初始化为 true
    for i in range(2, n):
        if isPrim[i]:
            # i 的倍数不可能是素数了
            j = 2 * i
            #j = i * i
            while j < n:
            # while j < sqrt(n):
                isPrim[j] = False
                j += i

    count = 0
    for i in range(2, n):
        if isPrim[i]:
            count += 1
    return count

print(countPrimes(10))
'''

int countPrimes(int n) {
    boolean[] isPrim = new boolean[n];
    Arrays.fill(isPrim, true);
    for (int i = 2; i * i < n; i++) 
        if (isPrim[i]) 
            for (int j = i * i; j < n; j += i) 
                isPrim[j] = false;

    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim[i]) count++;

    return count;
}
'''