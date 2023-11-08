from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda'

# WRITE YOUR CODE BELOW

def generate_letter_combinations():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    combinations = []

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            pair = alphabet[i] + alphabet[j]
            combinations.append(pair)

    return combinations

combinations = generate_letter_combinations()


for find_me in combinations:
    secret_password = find_me + 'bcmpda'
    print(secret_password)
    test = unzip_with_7z(zip_file_path, dest_path, secret_password)
    print(test)
# ----------------------------------------


