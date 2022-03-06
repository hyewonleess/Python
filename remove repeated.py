import time

# 리스트 중복 제거
mylist = [1, 3, 5, 6, 5, 5, 3, 4, 4, 5, 2, 2, 2, 1]


## 1. 기존 리스트의 순서 유지 하지 않는 경우
print(list(set(mylist)))
# output: [1, 2, 3, 4, 5, 6]


## 2. 중복 제거하되 기존 리스트의 순서 유지

### (1) for loop
start = time.time()
newlist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)

print(f"time: {time.time()-start:.5f}")
# 소요시간: 0.00100초

print(newlist)
# output: [1, 3, 5, 6, 4, 2]


### (2) dictionary

print(list(dict.fromkeys(mylist)))
# output: [1, 3, 5, 6, 4, 2]

### (3) sorted

print(sorted(set(mylist), key = lambda x: mylist.index(x)))
# output: [1, 3, 5, 6, 4, 2]



