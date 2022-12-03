import pathlib


def parse_data(input_file):
    """Parse input file and return data as a list of integers."""
    with open(input_file, 'r') as f:
        data = f.readlines()
    f.close()
    clean_data = []
    for line in data:
        # print(line)
        clean_data.append(line.strip())
    return clean_data

priority_score = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
    }
def part_1(data):
    rucksack = []
    # create priority score dictionary

    sum_of_priority_scores = 0
    for i, line in enumerate(data):
        n = len(line) // 2
        line_l = list(line)
        rucksack.append([line[:n], line[n:]])
        set1 = set(list(line[:n]))
        set2 = set(list(line[n:]))
        common = set1.intersection(set2)
        sum_of_priority_scores += sum([priority_score[c] for c in common])
        print(f"{i:2} {line:40} {n:2} {line[:n]:20} {line[n:]:20} {common}")
    print(f"Sum of priority scores: {sum_of_priority_scores}")



def part_2(data):
    score = 0
    # iterate through data in groups of 3
    for i in range(0, len(data), 3):
        set1 = set(list(data[i]))
        set2 = set(list(data[i + 1]))
        set3 = set(list(data[i + 2]))
        common = set1.intersection(set2, set3)
        score += sum([priority_score[c] for c in common])
        print(f"{i:2} {data[i]:40} {data[i+1]:40} {data[i+2]:40} {common}")
    print(f"Sum of priority scores: {score}")

if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent / "input_data.txt"
    data = parse_data(input_file)

    # part 1 of the puzzle
    # part_1(data)

    # part 2 of the puzzle
    part_2(data)
