from random import randint

def sort(arr):
    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                b = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = b

N = 100
a = []
for i in range(N):
    a.append(randint(-100,100))

print(a)
sort(a)
print(a)
