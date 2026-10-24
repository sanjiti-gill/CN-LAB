total = int(input("Total frames: "))
window = int(input("Window size: "))
lost = set(map(int, input("Frames to lose (space separated, blank for none): ").split()))

acked = set()
base = 0

while base < total:
    for f in range(base, min(base + window, total)):
        if f in acked:
            continue
        print("Sent frame", f)
        if f in lost:
            lost.remove(f)
            print(f"Frame {f} lost -> NAK {f}, resend only this one")
        else:
            acked.add(f)
            print("ACK", f)
    while base in acked:
        base += 1
