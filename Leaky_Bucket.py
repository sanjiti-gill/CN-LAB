# Leaky Bucket (policing) - follows Figure 39

limit = int(input("Enter bucket limit: "))
times = list(map(int, input("Enter arrival times (space separated): ").split()))

level = 0           # X
last = times[0]     # LCT

for t in times:
    new = max(level - (t - last), 0)    # X'
    if new > limit:
        print(f"t={t}: Nonconforming (discarded)")
    else:
        level = new + 1
        last = t
        print(f"t={t}: Conforming")
