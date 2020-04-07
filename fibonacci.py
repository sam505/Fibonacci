fib = [1,1]
m = 0
n = 1
for m in range (0,20):
    ans = fib [m] + fib [n]
    fib.append(ans)
    m += 1
    n += 1
print (fib)
