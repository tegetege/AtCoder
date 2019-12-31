A = int(input())
B = int(input())
C = int(input())
score = [A,B,C]
score_sorted = sorted(score,reverse=True)
print(score_sorted.index(score[0])+1)
print(score_sorted.index(score[1])+1)
print(score_sorted.index(score[2])+1)