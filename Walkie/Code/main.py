import re
import random
import time
import responses
import joke

bot_name = "Walkie"


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    # ----------------------------- #

    response(responses.greeting(), ["hello", "hi", "yo", "what's up",
             "whats up", "what's up", "sup", "ayo", "heyo", "hiya", "hey", "heya", "hola", "bonjour"], single_response=True)

    response(responses.goodbye(), [
             "bye", "goodbye", "cya", "later", "l8g8r", "cy@", "peace"], single_response=True)

    response(responses.response_to_laugh(), ["lol", "lmao", "rofl", "lmfao",
             "haha", "xd"], single_response=True)

    response("...", ["hm", "hmm", "hmmm", "hmmmm",
             "hmmmmm", "hmmmmmm"], single_response=True)

    response(responses.reassure(), [
             "awesome", "amazing", "fantastic", "great", "cool", "okay", "ok", "really", "good", "nice", "interesting", "yeah", "fr"], single_response=True)

    response(responses.accept_apology(), [
             "sorry", "apologies"], single_response=True)

    response(responses.negative_response(), [
             "no", "nope"], single_response=True)

    response(responses.unsure_user(), [
             "what", "where", "why", "how", "who"], single_response=True)

    response(responses.user_thanks(), [
             "thanks", "thank"], single_response=True)

    # ----------------------------- #

    response(responses.status(), ["how", "are",
             "you", "doing"], required_words=["how", "you"])

    response(responses.like(), ["what", "do",
             "you", "like", "doing"], required_words=["you", "like"])

    response(responses.question_adjective(), ["do", "you",
             "like", "to", "watch"], required_words=["you", "watch"])

    response(responses.question_adjective(), ["do", "you",
             "like", "to", "play"], required_words=["you", "play"])

    response(responses.question_adjective(), ["do", "you",
             "like", "to", "eat"], required_words=["you", "eat"])

    response(responses.question_adjective(), ["do", "you",
             "like", "to", "read"], required_words=["you", "read"])

    response(responses.question_adjective(), ["do", "you",
             "like", "to", "listen"], required_words=["you", "listen"])

    response(responses.age(), ["how", "old",
             "are", "you"], required_words=["you", "old"])

    response(responses.purpose(), ["what", "is",
             "your", "purpose"], required_words=["your", "purpose"])

    response(responses.purpose(), ["tell", "me",
             "about", "you"], required_words=["about", "you"])

    response(responses.creator(), ["who", "is",
             "your", "creator"], required_words=["your", "creator"])

    response(responses.creator(), ["who", "created",
             "you"], required_words=["you", "created"])

    response(responses.eat(), ["what", "do",
             "you", "eat"], required_words=["you", "eat"])

    response(responses.questioning(), ["what", "do",
             "you", "mean"], required_words=["you", "mean"])

    response(responses.learning_meaning(), ["it", "means"],
             required_words=["it", "means"])

    response(responses.identity(), ["who", "are", "you"],
             required_words=["who", "you"])

    response(responses.identity(), ["what", "are", "you"],
             required_words=["what", "are", "you"])

    response(responses.name(), ["what", "is", "your", "name"],
             required_words=["your", "name"])

    response(responses.asking_for_question(), ["i", "have", "a", "question"],
             required_words=["i", "question"])

    response(responses.favorite(), ["whats", "what's", "your", "favorite"],
             required_words=["your", "favorite"])

    response(joke.request_joke(), ["tell", "me", "a", "joke"],
             required_words=["a", "joke"])

    response(responses.like_favorite(), ["i", "like"],
             required_words=["i", "like"])

    response(responses.like_favorite(), ["my", "favorite"],
             required_words=["my", "favorite"])

    # ----------------------------- #

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_match] < 1:
        return responses.unkown()
    else:
        return best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    user_input = input("\nYou: ")
    time.sleep(random.randrange(1, 3))
    print("\n" + bot_name + ": " + get_response(user_input))
