print("Enter num")
n,m = map(int, input().split())

# print(N)
# print(M)

pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

print(pattern)

