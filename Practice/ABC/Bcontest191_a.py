v, t, s, d = map(int, input().split())
print('No') if v * t <= d and v * s >= d else print('Yes')