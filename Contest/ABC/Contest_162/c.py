import fractions
K = int(input())
ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        ab = fractions.gcd(i,j)
        if ab == 0:
            continue
        for k in range(1,K+1):
            if ab % k == 0 or k % ab == 0:
                if ab <= k:
                    print('yes')
                    ans += ab / k
                else:
                    print('no')
                    ans += k

print(ans)

# class C:
#     def __init__(self,K):
#         self.K = K
#         self.ans_dict = dict()
#         self.ans = 0
    
#     def start(self):
#         for i in range(1,K+1):
#             for j in range(1,K+1):
#                 for k in range(1,K+1):
#                     if str(i)+','+str(j)+','+str(k) not in self.ans_dict and str(j)+','+str(k)+','+str(i) not in self.ans_dict  and str(k)+','+str(i)+','+str(j) not in self.ans_dict:
#                         ans = self.cul_gcd(i,j,k)
#                         self.ans += ans
#                         self.ans_dict[str(i)+','+str(j)+','+str(k)] = ans
#                         self.ans_dict[str(j)+','+str(k)+','+str(i)] = ans
#                         self.ans_dict[str(k)+','+str(i)+','+str(j)] = ans
#                     else:
#                         # print(i,j,k)
#                         self.ans += self.ans_dict[str(i)+','+str(j)+','+str(k)]
#         print(self.ans)

#     def cul_gcd(self,a,b,c):
#         ab = fractions.gcd(a,b)
#         abc = fractions.gcd(ab,c)
#         return abc

# K = int(input())
# do = C(K)
# do.start() 
