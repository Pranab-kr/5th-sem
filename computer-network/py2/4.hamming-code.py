# Title: Hamming Code for Error Detection and Correction (Python 2)
def calculate_parity_bits(data):
    m = len(data)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def generate_hamming_code(data):
    data = data[::-1]
    m = len(data)
    r = calculate_parity_bits(data)
    total_bits = m + r
    hamming = ['0'] * (total_bits + 1)
    j = 0
    for i in range(1, total_bits + 1):
        if (i & (i - 1)) != 0:
            hamming[i] = data[j]
            j += 1
    for p in range(r):
        position = 2 ** p
        parity = 0
        for i in range(1, total_bits + 1):
            if i & position:
                parity ^= int(hamming[i])
        hamming[position] = str(parity)
    return ''.join(hamming[1:])

def detect_and_correct(received):
    n = len(received)
    received = ['0'] + list(received)
    error_position = 0
    parity_position = 1
    while parity_position <= n:
        parity = 0
        for i in range(1, n + 1):
            if i & parity_position:
                parity ^= int(received[i])
        if parity != 0:
            error_position += parity_position
        parity_position *= 2
    print "\nError position:", error_position
    if error_position == 0:
        print "No error detected."
    else:
        print "Error detected at position:", error_position
        if received[error_position] == '0':
            received[error_position] = '1'
        else:
            received[error_position] = '0'
        print "Corrected codeword:", ''.join(received[1:])

data = raw_input("Enter data bits: ")
codeword = generate_hamming_code(data)
print "\nGenerated Hamming Code:", codeword

received = raw_input("Enter received Hamming Code: ")
detect_and_correct(received)

# Example Output:
# Enter data bits: 1011
#
# Generated Hamming Code: 1010101
# Enter received Hamming Code: 1011101
#
# Error position: 4
# Error detected at position: 4
# Corrected codeword: 1010101