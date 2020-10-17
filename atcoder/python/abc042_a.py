# https://atcoder.jp/contests/abc042/tasks/abc042_a
l=list(map(int,input().split()))
print("YES"if l.count(5)==2 and l.count(7)==1 else"NO")