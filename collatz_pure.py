import gc

def collatz(n):
    """Iterate the Collatz sequence for n using cache.
    The cache stores numbers that are known to eventually reach 1.
    """
    original = n
    sequence = []
    # Follow the sequence until we hit 1 or a number already in the cache.
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return True, len(sequence)

def main():
    n = 1
    total_sequence_length = 0
    largest_sequence_length = 0
    while True:
        ret, sequence_length = collatz(n)
        total_sequence_length += sequence_length
        if sequence_length > largest_sequence_length:
            largest_sequence_length = sequence_length
        if not ret:
            print(f"Collatz conjecture fails for {n}")
            break
        # Optionally, print progress every so often.
        if n % 100000 == 0:
            print(f"Tested up to {n}, average sequence length is {total_sequence_length / 100000}, largest sequence length is {largest_sequence_length}")
            total_sequence_length = 0
            largest_sequence_length = 0

        if n % 1000000 == 0:
            gc.collect()

        n += 1

if __name__ == "__main__":
    main()
