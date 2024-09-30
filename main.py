def generate_powerrs_of_two(N):
    result = []
    for i in range(N + 1):
        result.append(2 ** i)
    return result
    
# User input
N = int(input("Enter an integer for power N: ")) 
    
# Generate a list of powers of two
result = generate_powerrs_of_two(N)
    
# Print the result
print("List of powers of 2 from 0 to", N, ":")
print(result)