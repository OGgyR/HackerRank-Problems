a = int(input())
b = int(input())
c = int(input())
arr = []
arr.append((a+b)*c)
arr.append(a*b*c)
arr.append((a+c)*b)
arr.append((b+c)*a)
arr.append(a+b+c)
print(max(arr))