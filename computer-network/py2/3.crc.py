# Title: CRC Error Detection using Modulo-2 Division (Python 2)
def xor_operation(a, b):
    result = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

def modulo2_division(data, generator):
    generator_length = len(generator)
    temp = data[:generator_length]
    while generator_length < len(data):
        if temp[0] == '1':
            temp = xor_operation(generator, temp) + data[generator_length]
        else:
            temp = xor_operation('0' * generator_length, temp) + data[generator_length]
        generator_length += 1
    if temp[0] == '1':
        temp = xor_operation(generator, temp)
    else:
        temp = xor_operation('0' * generator_length, temp)
    return temp

data = raw_input("Enter data bits: ")
generator = raw_input("Enter generator bits: ")
appended_data = data + '0' * (len(generator) - 1)
remainder = modulo2_division(appended_data, generator)
codeword = data + remainder
print "\nCRC Remainder:", remainder
print "Transmitted Codeword:", codeword

receiver = raw_input("\nEnter received codeword: ")
check_remainder = modulo2_division(receiver, generator)
print "Receiver Remainder:", check_remainder
if '1' in check_remainder:
    print "Error detected in received data."
else:
    print "No error detected. Data received correctly."

# Example Output:
# Enter data bits: 1101011011
# Enter generator bits: 10011
#
# CRC Remainder: 1110
# Transmitted Codeword: 11010110111110
#
# Enter received codeword: 11010110111110
# Receiver Remainder: 0000
# No error detected. Data received correctly.