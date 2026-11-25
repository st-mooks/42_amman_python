from sys import argv


def print_scores(argc: int, scores: list[int]) -> None:
    score_sum = sum(scores)
    max_score = max(scores)
    min_score = min(scores)
    avg_score = score_sum / (argc)
    print(f"Total players: {argc}")
    print(f"Total score: {score_sum}")
    print(f"Average score: {avg_score}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argv = argv[1:]
    argc = len(argv)
    scores: list[int] = []
    for arg in argv:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if argc > 0 and len(scores) == argc:
        print_scores(argc, scores)
    else:
        print("No scores provided.",
              "usage: python3 ft_score_analytics.py <score1> <score2> ...")
