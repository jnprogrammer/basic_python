with open("binary", 'bw') as bin_file:
        bin_file.write(bytes(range(17)))

with open("binary", 'br') as read_file:
    for b in read_file:
        print(b)