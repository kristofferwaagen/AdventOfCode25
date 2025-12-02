def solve_part1(instructions):
    """
    Part 1: Count how many times the dial points at 0 after rotations.
    """
    position = 50
    zero_count = 0
    
    for i in instructions:
        direction = i[0]
        distance = int(i[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count


def count_zeros_in_rotation(position, distance, direction):
    """
    Count how many times the dial passes through 0 during a rotation.
    
    Args:
        position: Starting position (0-99)
        distance: Distance to rotate
        direction: 'L' or 'R'
    
    Returns:
        Number of times passing through 0
    """
    # Calculate distance to first zero crossing
    distance_to_first_zero = (100 - position) % 100 if direction == 'R' else position
    
    # If already at 0, we need a full rotation to reach 0 again
    if distance_to_first_zero == 0:
        distance_to_first_zero = 100
    
    # Count zeros: first crossing + additional full cycles
    if distance >= distance_to_first_zero:
        remaining_distance = distance - distance_to_first_zero
        return 1 + (remaining_distance // 100)
    
    return 0


def solve_part2(instructions):
    """
    Part 2: Count how many times the dial passes through 0, including during rotations.
    """
    position = 50
    zero_count = 0
    
    for i in instructions:
        direction = i[0]
        distance = int(i[1:])
        
        zeros_in_rotation = count_zeros_in_rotation(position, distance, direction)
        zero_count += zeros_in_rotation
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
    
    return zero_count


def main():
    with open('input.txt', 'r') as f:
        instructions = [line.strip() for line in f if line.strip()]
    
    password1 = solve_part1(instructions)
    password2 = solve_part2(instructions)
    
    print(f"Part 1: {password1}")
    print(f"Part 2: {password2}")


if __name__ == "__main__":
    main()
