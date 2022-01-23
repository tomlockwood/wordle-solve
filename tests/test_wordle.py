import wordle

def test_wordle_play():
    triplets = [
        ["butss","somes","00012"],
        ["crony","civic","20000"],
    ]
    for triplet in triplets:
        assert str(wordle.play(triplet[0],triplet[1])) == f"{triplet[0]}: {triplet[2]}"

    