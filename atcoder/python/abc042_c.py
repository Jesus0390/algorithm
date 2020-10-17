# https://atcoder.jp/contests/abc042/tasks/arc058_a

def error_handle(msg):
	print("Error : " + msg)
	exit()

N, K=list(map(int, input().split()))

if N<1:
	error_handle("amount money must be greater than 1")	
elif N>10000:
	error_handle("amount money must be less than 10000")

D=list(map(int, input().split()))
if len(D)!=K:
	error_handle("the input D length than Iroha dislikes " \
		"is different to input K number, D length -> " +   \
		str(len(D)) + ", K number -> " + str(K))

D.sort()

if K==9 and not D.count(0)>1:
	print(D)
	error_handle("input D numbers can't be {1,2,3,4,5,6,7,8,9} format")

for i in D:
	if D.count(i)>1:
		error_handle("don't repeat input D number. the repeated number is " + str(i))
	if i<0:
		error_handle("input D numbers can't be less than 0")
	if i>=10:
		error_handle("input D numbers can't be equal or greater than 10")

''' 
firts implementation
input
1000 8
1 3 4 5 6 7 8 9

output
2000
'''
arr_allow_number=[]
for i in range(10):
	if not i in D:
		arr_allow_number.append(i)

i=N
r=""
for index_range in range(10000):
	i_str=str(index_range)
	for index_str in range(len(i_str)):
		if i_str[index_str] in D:
			r=""
			break
		else:
			for j in arr_allow_number:
				if int(i_str[index_str])<j:
					r+=str(j)
					break
print(r)