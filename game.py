import random

roll_die = lambda: random.randint(1, 6)


def dice_game(rounds):
    player01 = input("Enter your name : ")
    player02 = input("Enter your name : ")

    p1Win = 0
    p2Win = 0
    rn = 1

    while rn <= rounds:
        print("---------Round number {}-----------".format(rn))

        if rn != 1:
            input("Please just press ENTER to the next round")

        p1 = roll_die()
        p2 = roll_die()
        print("{} roll : {} & {} roll : {}.".format(player01, p1, player02, p2))
        if p1 == p2:
            print("The round is drow.")

        elif p1 > p2:
            print("The round is won by {}.".format(player01))
            p1Win += 1

        else:
            print("The round is won by {}.".format(player02))
            p2Win += 1

        rn += 1
        print(
            "***************************************************************************************************"
        )

    if p1Win == p2Win:
        print("The game was drawn.")
    elif p1Win >= p2Win:
        print(
            "congradulations.....! The game won by {} by {} to {}".format(
                player01, p1Win, p2Win
            )
        )
    else:
        print(
            "congradulations.....! The game won by {} by {} to {}".format(
                player02, p2Win, p1Win
            )
        )
