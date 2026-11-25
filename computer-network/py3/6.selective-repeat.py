# Title: Selective Repeat ARQ Protocol (Python 3)
import random

def selective_repeat(frames, window_size):
    acked = [False] * len(frames)
    i = 0
    while not all(acked):
        for j in range(i, min(i + window_size, len(frames))):
            if not acked[j]:
                print("Sent frame {}".format(frames[j]))
                if random.choice([True, False]):
                    print("Acknowledgement received for frame {}".format(frames[j]))
                    acked[j] = True
                else:
                    print("Error in frame {} - will retransmit".format(frames[j]))
        while i < len(frames) and acked[i]:
            i += 1
    print("All frames sent successfully.")

frames = [1, 2, 3, 4, 5]
selective_repeat(frames, 3)

# Example Output:
# Sent frame 1
# Acknowledgement received for frame 1
# Sent frame 2
# Acknowledgement received for frame 2
# Sent frame 3
# Error in frame 3 - will retransmit
# Sent frame 4
# Error in frame 4 - will retransmit
# Sent frame 5
# Acknowledgement received for frame 5
# ...
# All frames sent successfully.