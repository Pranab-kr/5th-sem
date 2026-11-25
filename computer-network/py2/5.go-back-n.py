# Title: Go-Back-N ARQ Protocol (Python 2)
import random

def go_back_n(frames, window_size):
    sent = 0
    while sent < len(frames):
        for i in range(window_size):
            if sent + i < len(frames):
                print "Sent frame {}".format(frames[sent + i])
        ack = random.choice([True, False])
        if ack:
            print "Acknowledgement received for frame {}".format(frames[sent])
            sent += 1
        else:
            print "Error! Resending from frame {}".format(frames[sent])
    print "All frames sent successfully."

frames = [1, 2, 3, 4, 5]
go_back_n(frames, 3)

# Example Output:
# Sent frame 1
# Sent frame 2
# Sent frame 3
# Acknowledgement received for frame 1
# Sent frame 2
# Sent frame 3
# Sent frame 4
# Error! Resending from frame 2
# Sent frame 2
# Sent frame 3
# Sent frame 4
# Acknowledgement received for frame 2
# ...
# All frames sent successfully.