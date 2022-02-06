N = int(input())
a_list = list(map(int,input().split()))
it = iter(a_list)

alice = list()
bob   = list()

for i in range(int(len(a_list)+1/2)):
	try:
		alice.append(max(a_list))
		a_list.remove(max(a_list))
		bob.append(max(a_list))
		a_list.remove(max(a_list))
	except ValueError:
		break

print(sum(alice)-sum(bob))
