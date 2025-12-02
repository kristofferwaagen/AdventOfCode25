def is_invalid_id(product_id):
    """Check if a product ID is invalid (sequence repeated at least twice)."""
    id_string = str(product_id)
    num_digits = len(id_string)
    
    # Try all possible pattern lengths (from 1 to half the length)
    for pattern_length in range(1, num_digits // 2 + 1):
        # Check if the total length is divisible by pattern length
        if num_digits % pattern_length == 0:
            pattern = id_string[:pattern_length]
            repetitions = num_digits // pattern_length
            
            # Check if repeating the pattern creates the entire string
            if pattern * repetitions == id_string:
                return True
    
    return False


def solve(input_ranges):
    """Find sum of all invalid IDs across all ranges."""
    total_sum = 0
    
    for range_text in input_ranges.strip().split(','):
        if not range_text.strip():
            continue
            
        range_start, range_end = map(int, range_text.strip().split('-'))
        
        for product_id in range(range_start, range_end + 1):
            if is_invalid_id(product_id):
                total_sum += product_id
    
    return total_sum


def main():
    with open('input.txt', 'r') as f:
        input_ranges = f.read()
    
    result = solve(input_ranges)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
