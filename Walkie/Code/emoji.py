from random import randint, choice


def add_emoji(feeling):

    happy = [":)", ":D", ":>", ":]", "XD", "xD"]  # Feeling value 0 or "happy"
    neutral = [":P", ":L", ":/", ":|"]  # Feeling value 1 or "neutral"
    sad = [":(", "D:", ":<", ":["]  # Feeling value 2 or "sad"

    if randint(1, 5) == 3:

        if feeling == 0 or feeling == "happy":
            return f" {choice(happy)}"

        elif feeling == 1 or feeling == "neutral":
            return f" {choice(neutral)}"

        elif feeling == 2 or feeling == "sad":
            return f" {choice(sad)}"

        else:
            print("\nInvalid feeling input value: {feeling}.")

    else:
        return " "
