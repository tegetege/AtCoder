def key_func(n):
	return len(n)
A = str(input())
B = str(input())
target = [A,B]
print(max(target, key=key_func))