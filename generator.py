import itertools
import string


def generate_combinations(output_filename="combinations.txt"):
    # Define the prefix (6 zeroes)
    prefix = "000000"

    # Define the characters for the last 4 positions: a-z, A-Z, 0-9
    charset = string.ascii_letters + string.digits

    print("Generating combinations... This may take a minute.")

    # Open the file and write combinations efficiently using a generator
    with open(output_filename, "w", encoding="utf-8") as f:
        # itertools.product generates all possible 4-character combinations
        for combo in itertools.product(charset, repeat=4):
            # Combine the prefix and the 4 characters, then write to file
            line = prefix + "".join(combo) + "\n"
            f.write(line)

    print(f"Success! All combinations saved to '{output_filename}'.")


if __name__ == "__main__":
    generate_combinations()
