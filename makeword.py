import itertools

# Define the possible elements
months = ['1', '2', '03', '4', '5', '6', '7', '8', '9', '10', '11', '12']
chars = ['kAor1', 's3nKu', 'sTev3', 'Lev1', 'L1Ly']
specials1 = ['*', '#', '!', '%', '&', '+']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specials2 = ['*', '#', '!', '%', '&', '+']

# Generate all possible combinations
combinations = itertools.product(months, chars, specials1, nums, letters, specials2)

# Convert combinations to strings and write to file
with open('wordlist.txt', 'w') as f:
    for combo in combinations:
        password = ''.join(combo)
        f.write(password + '\n')