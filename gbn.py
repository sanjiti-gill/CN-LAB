total, window = 8, 4

lost = {2}          # frame 2 gets lost once

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
