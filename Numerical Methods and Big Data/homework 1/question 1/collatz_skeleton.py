def collatz(n):
# collatz.py returns a vector (collatz_seq) containing the Collatz sequence and
# its length (collatz_len) given. We have provided the skeleton code.
# Please fill in all of the _____'s with an appropriate code.

    # Initialize variables to return
    collatz_seq = []; #empty list
    collatz_len = n;
    
    # Update n and return values
    while(n != 1): #termination criterion

        # Compute the next number in the sequence
        if ((n % 2) == 0):
            n = n/2
        else:
            n = 3*n + 1
        
        collatz_seq.append(n); # Append the new n to the sequence
        collatz_len = collatz_len + 1; # Update the length

    return collatz_seq, collatz_len

