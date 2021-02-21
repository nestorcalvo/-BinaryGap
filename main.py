def solucion(N):
    # Flag to identify the first "1"
    first = True
    # Variable to store the max distance
    max_distance = 0
    # Variable to store the recent max distance
    count = 0
    # While to convert to binary from decimal number
    while N != 0:
        # Residue from the division (this is one digit of the final binary number but backwards)
        res = N % 2
        # Stop condition
        N = int(N / 2)
        # If the flag firs is off (there is already a number 1)
        if not first:
            # If we found another 1 (second 1)
            if res == 1:
                # Set the flag first to True to count again if multiple there are multiple 1's in the binary
                # representation
                first = True
                # Save the max distance found
                max_distance = count if max_distance < count else max_distance
            else:
                # If we found a 0, increase the counter
                count += 1
        # If we found the first 1 we start counting
        if res == 1 and first:
            count = 0
            first = False
    # Return the max distance found
    return max_distance


if __name__ == '__main__':
    # Change N to test
    N = 2
    print('Max distance: ', solucion(N))
