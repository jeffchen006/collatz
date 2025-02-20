import gc

def collatz(n, cache):
    """Iterate the Collatz sequence for n using cache.
    The cache stores numbers that are known to eventually reach 1.
    """
    original = n
    sequence = []
    # Follow the sequence until we hit 1 or a number already in the cache.
    while n != 1 and n not in cache:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    # Mark every number in the current sequence as eventually reaching 1.
    for num in sequence:
        cache[num] = True
    return True, cache, len(sequence)

def main():
    cache = {1: True}  # We know 1 eventually reaches 1.
    n = 1
    total_sequence_length = 0
    largest_sequence_length = 0
    while True:
        ret, cache, sequence_length = collatz(n, cache)
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
