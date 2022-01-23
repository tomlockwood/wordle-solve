import time
from lib import targetlist
from lib.games import FrequencyGame


def main():
    games = [
        (FrequencyGame, {"expanded_list_guesses": 0}),
        # (FrequencyGame, {"expanded_list_guesses": 1}),
        # (FrequencyGame, {"expanded_list_guesses": 2}),
        # (FrequencyGame, {"expanded_list_guesses": 3}),
        # (FrequencyGame, {"expanded_list_guesses": 4}),
        # (FrequencyGame, {"expanded_list_guesses": 5}),
        # (FrequencyGame, {"expanded_list_guesses": 6}),
    ]

    results = {
        f"{game.__name__} - {opts}": {k + 1: 0 for k in range(6)}
        for game, opts in games
    }
    for _, v in results.items():
        v["losses"] = 0
    for game, opts in games:
        game_string = f"{game.__name__} - {opts}"
        game_instance = game(**opts)
        for word in targetlist:
            game_instance.run(word)
            guesses = game_instance.guesses
            if not guesses[-1].won:
                results[game_string]["losses"] += 1
                # Show me the losses:
                # print(f"{word}: {guesses}")
            else:
                results[game_string][len(guesses)] += 1

    print(results)

    for game, opts in games:
        print(f"{game.__name__} - {opts}")
        count = 0
        sum_of = 0
        for k, v in results[f"{game.__name__} - {opts}"].items():
            if not isinstance(k, int):
                continue
            count += v
            sum_of += k * v
        if count != 0:
            print(f"Average: {sum_of/count}")
        print(f"Total: {count}")


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Seconds: {time.time() - start}")
