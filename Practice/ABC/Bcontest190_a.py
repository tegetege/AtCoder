a, b, c = map(int, input().split())

if a == b:
    print("Takahashi") if c == 1 else print("Aoki")
else:
    print("Takahashi") if a > b else print("Aoki")