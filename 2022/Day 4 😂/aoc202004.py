import pathlib


def parse_data(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
    f.close()
    clean_data = []
    for line in data:
        clean_data.append(line.strip().split(','))
        # print(line.strip().split(','))
    return clean_data


def part_1(data):
    total_subsets = 0
    for line in data:

        line1 = line[0].split('-')
        # start of first pair
        fs = line1[0]
        # end of first pair
        fe = line1[-1]
        fp_l = [i for i in range(int(fs), int(fe)+1, 1)]

        line2 = line[1].split('-')
        # start of second pair

        ss = line2[0]
        # end of second pair
        se = line2[-1]
        sp_l = [i for i in range(int(ss), int(se)+1, 1)]

        set1 = set(fp_l)
        set2 = set(sp_l)
        subSet = None
        # cheek for subset either way
        if set1.issubset(set2) or set2.issubset(set1):
            subSet = True
            total_subsets += 1

        print(line[0], line[1], fp_l, sp_l, subSet)
    print(f"total_subsets: {total_subsets}")

def part_2(data):
    total_subsets = 0
    for line in data:

        line1 = line[0].split('-')
        # start of first pair
        fs = line1[0]
        # end of first pair
        fe = line1[-1]
        fp_l = [i for i in range(int(fs), int(fe)+1, 1)]

        line2 = line[1].split('-')
        # start of second pair

        ss = line2[0]
        # end of second pair
        se = line2[-1]
        sp_l = [i for i in range(int(ss), int(se)+1, 1)]

        set1 = set(fp_l)
        set2 = set(sp_l)
        subSet = None
        intersection = set1.intersection(set2)
        if intersection:
            subSet = True
            total_subsets += 1
        # cheek for subset either way
        # if set1.issubset(set2) or set2.issubset(set1):
        #     subSet = True
        #     total_subsets += 1

        print(line[0], line[1], fp_l, sp_l, subSet, intersection)
    print(f"total_subsets: {total_subsets}")


if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent / "input_data.txt"
    data = parse_data(input_file)

    # part 1 of the puzzle
    # part_1(data)

    # part 2 of the puzzle
    part_2(data)
