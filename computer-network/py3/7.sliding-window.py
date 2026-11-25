# Title: Sliding Window Protocol (Python 3)
def sliding_window(frames, window_size):
    start = 0
    while start < len(frames):
        end = min(start + window_size, len(frames))
        print("Sending frames {}".format(frames[start:end]))
        print("Acknowledgement received for frames {}".format(frames[start:end]))
        start += window_size
    print("All frames sent successfully.")

frames = [1, 2, 3, 4, 5]
sliding_window(frames, 3)

# Example Output:
# Sending frames [1, 2, 3]
# Acknowledgement received for frames [1, 2, 3]
# Sending frames [4, 5]
# Acknowledgement received for frames [4, 5]
# All frames sent successfully.