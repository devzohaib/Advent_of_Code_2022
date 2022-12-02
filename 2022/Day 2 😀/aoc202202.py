import pathlib


def parse_input(input_file):
    with open(input_file) as f:
        # read file line by line and store in a list
        lines = f.readlines()
    f.close()

    # turns
    played = []
    for line in lines:
        # print(line.strip().split())
        played.append(line.strip().split())
    return played


def part_1(played):
    """ played is a list round of your turn and opponent's turn
    Score for choices:
        Rock : 1
        Paper : 2
        Scissors : 3
    Outcome of a round:
        0: if you lose
        3: if round is a draw
        6: if you win
    Opponent Turns:
        A: Rock
        B: Paper
        C: Scissors
    Your Turns:
        X: Rock
        Y: Paper
        Z: Scissors
    Winning combinations:
        Rock defeats Scissors
        Scissors defeats Paper
        Paper defeats Rock

    """
    print("Part 1")
    print("----------------")
    print(played)
    opponent_moves = {'A': "Rock", 'B': "Paper", 'C': "Scissors"}
    your_moves = {'X': "Rock", 'Y': "Paper", 'Z': "Scissors"}
    score_for_choices = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    total_score = 0
    for each_round in played:
        your_turn = your_moves[each_round[1]]
        opponent_turn = opponent_moves[each_round[0]]
        match = None
        score_earned = 0
        # Draw
        if your_turn == opponent_turn:
            score_earned = score_for_choices[your_turn] + 3
            total_score += score_earned
            match = "Draw"
            # print("Draw")
        elif your_turn == "Rock" and opponent_turn == "Scissors":
            score_earned = score_for_choices[your_turn] + 6
            total_score += score_earned
            match = "Win"
            # print("You win")
        elif your_turn == "Scissors" and opponent_turn == "Paper":
            score_earned = score_for_choices[your_turn] + 6
            total_score += score_earned
            match = "Win"
            # print("You win")
        elif your_turn == "Paper" and opponent_turn == "Rock":
            score_earned = score_for_choices[your_turn] + 6
            total_score += score_earned
            match = "Win"
        else:
            match = "Loss"
            if your_turn == "Rock":
                score_earned = score_for_choices[your_turn]
                total_score += score_earned
            elif your_turn == "Scissors":
                score_earned = score_for_choices[your_turn]
                total_score += score_earned
            elif your_turn == "Paper":
                score_earned = score_for_choices[your_turn]
                total_score += score_earned
            # print("You lose")

        # print(each_round, "Opponent Turn:", opponent_turn, "Your Turn:", your_turn, "Match:", match, "Score:", score_earned)
        # format the string with fixed width
        print(
            f"{each_round} Opponent Turn: {opponent_turn:10} Your Turn: {your_turn:10} Match: {match:5} Score: {score_earned:2}")
        # print(f"{each_round} Opponent Turn: {opponent_turn} Your Turn: {your_turn} Match: {match} Score: {score_earned}")

    print("Total Score:", total_score)


def part_2(played):
    """
     played is list of round of opponent's turn and your goal to achieve by playing a turn
    Score for choices:
        Rock : 1
        Paper : 2
        Scissors : 3
    Outcome of a round:
        0: if you lose
        3: if round is a draw
        6: if you win
    Opponent Turns:
        A: Rock
        B: Paper
        C: Scissors
    Your Goal:
        X: you need to lose
        Y: you need to draw
        Z: you need to win
    Winning combinations:
        Rock defeats Scissors
        Scissors defeats Paper
        Paper defeats Rock

    """
    print("Part 2")
    print("----------------")
    print(played)
    opponent_moves = {'A': "Rock", 'B': "Paper", 'C': "Scissors"}
    your_goal = {'X': "lose", 'Y': "draw", 'Z': "win"}
    score_for_choices = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    total_score = 0
    for each_round in played:
        earned_score = 0
        opponent_turn = opponent_moves[each_round[0]]
        goal = your_goal[each_round[1]]
        # goal is draw
        if goal == "draw":
            # your turn will be the same as opponent's turn
            earned_score = score_for_choices[opponent_turn] + 3
            total_score += earned_score
            pass
        # goal is loose
        if goal == "lose":
            # Rock defeats Scissors
            if opponent_turn == "Rock":
                earned_score = score_for_choices["Scissors"]
                total_score += earned_score
            # Scissors defeats Paper
            elif opponent_turn == "Scissors":
                earned_score = score_for_choices["Paper"]
                total_score += earned_score
            # Paper defeats Rock
            elif opponent_turn == "Paper":
                earned_score = score_for_choices["Rock"]
                total_score += earned_score
        # goal is win
        if goal == "win":
            # Rock defeats Scissors
            if opponent_turn == "Scissors":
                earned_score = score_for_choices["Rock"] + 6
                total_score += earned_score
            # Scissors defeats Paper
            elif opponent_turn == "Paper":
                earned_score = score_for_choices["Scissors"] + 6
                total_score += earned_score
            # Paper defeats Rock
            elif opponent_turn == "Rock":
                earned_score = score_for_choices["Paper"] + 6
                total_score += earned_score

        print(f"{each_round} Opponent Turn: {opponent_turn:10} Your Goal: {goal:5} Score: {earned_score:2}")
    # total score
    print("Total Score:", total_score)
if __name__ == '__main__':
    input_file = pathlib.Path(__file__).parent / 'input_data.txt'
    data = parse_input(input_file)

    # part 1 of the puzzle
    # part_1(data)

    # part 2 of the puzzle
    part_2(data)