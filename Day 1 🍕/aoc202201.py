import pathlib


def parse_input(input_file):
    with open(input_file) as f:
        # print(f.readline())
        readlines = f.readlines()
    f.close()
    return readlines


def part_1(readlines):
    # print(readlines)
    print(readlines)
    # remove newline characters
    readlines = [line.strip() for line in readlines]
    print(readlines)

    calories_list = []
    calories_stock = 0
    for i in range(len(readlines)):

        if readlines[i] != '':
            calories = int(readlines[i])
            calories_stock += calories
        elif readlines[i] == '':
            calories_list.append(calories_stock)
            calories_stock = 0
    calories_list.append(calories_stock)
    print(calories_list)
    print(max(calories_list))

    part_2(calories_list)

def part_2(data):
    print("Part 2")
    print(data)
    # sort the list
    data.sort()
    print(data)
    # find top 3 values sum
    # top_3_sum = data[-1] + data[-2] + data[-3]
    top_3_sum = sum(data[-3:])
    print(top_3_sum)


if __name__ == '__main__':
    input_file = pathlib.Path(__file__).parent / 'input_data.txt'
    data = parse_input(input_file)
    # print(data)
    part_1(data)
