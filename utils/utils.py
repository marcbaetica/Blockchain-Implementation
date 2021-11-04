from hashlib import sha256
from random import randint, choice
from string import ascii_uppercase, ascii_letters
from time import perf_counter


characters = [char for char in ascii_uppercase]


def generate_random_transactions():
    transactions = []
    for _ in range(randint(1, 3)):
        characters_copy = characters.copy()
        character_1 = choice(characters_copy)
        characters_copy.remove(character_1)
        character_2 = choice(characters_copy)
        transactions.append(f'{character_1} gave {character_2} ${randint(1, 10000)}.')
    return transactions


# TODO: Implemented but very computationally expensive. 137 seconds for 9 values only.
def generate_proof_of_work(duplicate_entries_count):
    beginning_sequence = generate_duplicate_entries_list(duplicate_entries_count)
    while True:
        # number_for_hashing = randint(1, 999999999999999999999)
        number_for_hashing = str([choice(ascii_letters) for _ in range(randint(1, 99))])
        new_hash = sha256(str(number_for_hashing).encode()).hexdigest()
        if any(sequence in new_hash for sequence in beginning_sequence):
            print(new_hash)
            return


def generate_duplicate_entries_list(repetition_count):
    return [repetition_count * str(i) for i in range(10)]


# Testing purposes
if __name__ == '__main__':
    # for _ in range(10):
    #     pprint(generate_random_transactions())

    for duplicates_count in range(10):
        start_time = perf_counter()
        generate_proof_of_work(duplicates_count+1)
        print(perf_counter() - start_time)
