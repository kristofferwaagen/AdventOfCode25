def is_invalid_id(product_id):
    """Check if a product ID is invalid (sequence repeated twice)."""
    id_string = str(product_id)
    num_digits = len(id_string)
    
    if num_digits % 2 != 0:
        return False
    
    midpoint = num_digits // 2
    return id_string[:midpoint] == id_string[midpoint:]


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
    print(f"Sum of all invalid IDs: {result}")


if __name__ == "__main__":
    main()
