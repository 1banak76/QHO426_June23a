def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def pattern(s, o):
    return{"sequence": s, "occurrences": o}


def run():
    print("Analysing Patterns....")
    d = {"short pattern": short_pattern(), "medium pattern": medium_pattern(), "long_pattern": long_pattern()}
    for k, v in d.items():
        print(f"{k}:{v}")


run()