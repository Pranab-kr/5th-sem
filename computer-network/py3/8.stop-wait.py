# Title: Stop & Wait Protocol Simulation (Python 3)
import random
import time

def sender(frames):
    print("Stop & Wait protocol simulation")
    i = 0
    while i < len(frames):
        frame = frames[i]
        print(f"\nSender: Sending frame {frame}")
        time.sleep(2)
        ack = random.choice([True, False])
        if ack:
            print(f"Receiver: Frame {frame} received successfully")
            print(f"Sender: Ack {frame} received. Sending next frame.")
            i += 1
        else:
            print(f"Receiver: Frame {frame} lost or Ack not received")
            print(f"Sender: Timeout! Resending frame {frame}")

def main():
    frames = [0, 1, 2, 3, 4]
    sender(frames)

main()

# Example Output:
# Stop & Wait protocol simulation
#
# Sender: Sending frame 0
# Receiver: Frame 0 received successfully
# Sender: Ack 0 received. Sending next frame.
#
# Sender: Sending frame 1
# Receiver: Frame 1 lost or Ack not received
# Sender: Timeout! Resending frame 1
#
# Sender: Sending frame 1
# Receiver: Frame 1 received successfully
# Sender: Ack 1 received. Sending next frame.
# ...