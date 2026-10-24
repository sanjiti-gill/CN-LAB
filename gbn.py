total = int(input("Total frames: "))
window = int(input("Window size: "))
lost = set(map(int, input("Frames to lose (space separated, blank for none): ").split()))

base = 0

while base < total:
    end = min(base + window, total)
    
    for f in range(base, end):
        print("Sent frame", f)
        
    for f in range(base, end):
        if f in lost:
            lost.remove(f)
            print(f"Frame {f} lost -> discarding the rest, going back to {f}")
            base = f
            break
        print("ACK", f)
        
    else:
        base = end
