total, window = 8, 4

lost = {2}          # frame 2 gets lost once

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
