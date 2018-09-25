# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def process_hands(cribbage_input, cards_in_hand):    

    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)

# --------------------------------------

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 3)
    cribbage_file.close()

# --------------------------------------

def print_hand(hand_as_list):
    print("Cribbage Hand")
    print("-------------")
    for i in range(3):
        print("Card " + str(i+1) + ": " + str(hand_as_list[i][0]) + " of " + str(hand_as_list[i][1]))

# --------------------------------------

def evaluate_hand(hand_as_list):

    # three of a kind
    if hand_as_list[0][0] == hand_as_list[1][0] and hand_as_list[2][0] == hand_as_list[1][0]:
        three_of_a_kind_point = 6
    else:
        three_of_a_kind_point = 0

    # pair
    if three_of_a_kind_point != 0:
        pair_point = 0
    else:
        if hand_as_list[0][0] == hand_as_list[1][0] or hand_as_list[0][0] == hand_as_list[2][0] or hand_as_list[1][0] == hand_as_list[2][0]:
            pair_point = 2
        else:
            pair_point = 0

    # sequence
    if hand_as_list[0][0] == hand_as_list[1][0] + 1 and hand_as_list[0][0] == hand_as_list[2][0] +2:
        sequence_point = 3
    elif hand_as_list[0][0] == hand_as_list[1][0] + 2 and hand_as_list[0][0] == hand_as_list[2][0] +1:
        sequence_point = 3
    elif hand_as_list[1][0] == hand_as_list[0][0] + 1 and hand_as_list[1][0] == hand_as_list[2][0] +2:
        sequence_point = 3
    elif hand_as_list[1][0] == hand_as_list[0][0] + 2 and hand_as_list[1][0] == hand_as_list[2][0] +1:
        sequence_point = 3
    elif hand_as_list[2][0] == hand_as_list[1][0] + 1 and hand_as_list[2][0] == hand_as_list[0][0] +2:
        sequence_point = 3
    elif hand_as_list[2][0] == hand_as_list[1][0] + 2 and hand_as_list[2][0] == hand_as_list[0][0] +1:
        sequence_point = 3
    else:
        sequence_point = 0

    # fifteen
    if hand_as_list[0][0] + hand_as_list[1][0] == 15:
        total_fifteen_point = 2
        if hand_as_list[0][0] + hand_as_list[2][0] == 15:
            total_fifteen_point = 4
        elif hand_as_list[1][0] + hand_as_list[2][0] == 15:
            total_fifteen_point = 4

    elif hand_as_list[1][0] + hand_as_list[2][0] == 15:
        total_fifteen_point = 2
        if hand_as_list[0][0] + hand_as_list[1][0] == 15:
            total_fifteen_point = 4
        elif hand_as_list[0][0] + hand_as_list[2][0] == 15:
            total_fifteen_point = 4

    elif hand_as_list[0][0] + hand_as_list[2][0] == 15:
        total_fifteen_point = 2
        if hand_as_list[0][0] + hand_as_list[1][0] == 15:
            total_fifteen_point = 4
        elif hand_as_list[1][0] + hand_as_list[2][0] == 15:
            total_fifteen_point = 4

    elif hand_as_list[0][0] + hand_as_list[1][0] + hand_as_list[2][0] == 15:
        total_fifteen_point = 2
    else:
        total_fifteen_point = 0




    total_points = three_of_a_kind_point + pair_point + sequence_point + total_fifteen_point
    print("Points scored:", total_points)
    print()

# --------------------------------------
main()
