n = int(input())
case = list(map(int, input().split()))
case.remove(max(case))
case.remove(min(case))
print(sum(case))
