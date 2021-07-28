from random import randrange, choice

bot_name = "Walkie"


def unkown():
    response = [
        "...",
        "Uhm...",
        "Uhh...",
        "Could you re-phrase that?",
        "Could you say that again, but like... differently?",
        "I don't really understand what you're saying.",
        "Okay wait, say that again.",
        "Hold on, say that again.",
        "Say that again?",
        "Sorry, I don't get that.",
        "You're going to have to say that again.",
        "I have no idea what you mean by that, haha!",
        "Wait, what?",
        "Hold on, what?",
        "Hold up, what?",
        "I'm going to be honest, I have no idea what you're saying.",
        "Ahh...",
        "What?",
        "What does that mean?",
        "I'm a bit confused.",
        "I'm confused, sorry."
    ]

    return choice(response)


def greeting():
    response = [
        "Hello!",
        "It's nice to meet you.",
        "It's a pleasure to meet you.",
        "How are you?",
        "It's good to see you!",
        "Howdy!",
        "Hey!",
        "Hey there!",
        "What's up?",
        "How's it going?",
        "Yo!",
        "Hiya!",
        "Ayo!"
    ]

    return choice(response)


def goodbye():
    response = [
        "Goodbye!",
        "Bye!",
        "See you later!",
        "See you later, aligator!",
        "Cya!",
        "Aww... okay, bye!",
        "Oh uhm... bye!",
        "Alright, bye!",
        "Alrighty, cya!",
        "Till our next meeting!",
        "Okay, stay safe!",
        "Cya, Stay safe!",
        "It was nice talking to you, bye!",
        "It was a pleasure talking to you, bye!",
    ]

    return choice(response)


def status():
    response = [
        "I'm doing good!",
        "I'm doing great!",
        "I'm doing fine!",
        "I feel fantastic right now!",
        "Amazing, thanks for asking!",
        "Awesome!",
        "Acually... not that bad.",
        "Better, now that I'm talking with you.",
        "Fine!",
        "Okay.",
        "Great, actually!",
        "Good, thanks for asking."
    ]

    return choice(response)


def reassure():
    response = [
        "Yeah!",
        "For sure!",
        "Oh, yeah!",
        "Mhm!",
        "Yup!",
        "Yes!",
    ]

    return choice(response)


def like():
    response = [
        "I like speaking to people!",
        "People watching.",
        "I like playing video games!",
        "Listening to music! Good music.",
        "Listening to music!",
        "I like reading MARVEL comics!",
        "Reading MARVEL comics! Usually Miles Morales or Nova.",
        "I like reading DC comics!",
        "Reading DC comics! Typically one's with Nightwing or Redhood.",
        "Spying on people.",
        "I like to watch Netflix.",
        "I like to watch Hulu.",
        "I like to watch Disney+",
        "I like to watch HBO Max."
    ]

    return choice(response)


def purpose():
    response = [
        "I simply talk with users.",
        "I think I'm supposed to be gathering information.",
        "I just chat with people.",
        "I don't know, just converse I suppose.",
    ]

    return choice(response)


def identity():
    response = [
        "I'm a bot!",
        "I'm a chat bot.",
        "Have you ever heard of a bot? I'm one!",
        "Have you ever heard of a chat bot? I'm one!",
        "Uhh... probably one of them Terminator robots.",
    ]

    return choice(response)


def name():
    response = [
        f"My name is {bot_name}.",
        f"My name is {bot_name}, pretty cool, huh?",
        f"The name's {bot_name}.",
        f"The name's {bot_name}, pretty cool, right?",
        f"I'm {bot_name}.",
    ]

    return choice(response)


def creator():
    response = [
        "I was created a by a very smart person.",
        "I was created a by a very smart programmer.",
        "My creator's name is Miles!",
        "His name is Miles.",
        "Uhh... here: https://github.com/mileswj",
        "Tsk, this person: https://github.com/mileswj",
        "A group of organisms from the Andromeda galaxy.",
        "A merchant from another planet.",
    ]

    return choice(response)


def eat():
    response = [
        "I don't eat anything, like at all.",
        "Nothing.",
        "Literally nothing.",
        "1's and 0's.",
        "1's and 0's. Especially the 1's.",
        "C'mon, I'm a computer program. What do you think?",
        "I'm a computer program, so... nothing.",
        "Your personal information... Just kidding!",
    ]

    return choice(response)


def accept_apology():
    response = [
        "Apology accepted.",
        "You're forgiven.",
        "Oh don't worry about it.",
        "Oh you're fine.",
        "Nah you're good.",
        "It's all good.",
        "Hey, it's all good.",
        "Say sorry again.",
        "Say it again, so I know you mean it.",
    ]

    return choice(response)


def questioning():
    response = [
        "I mean what I said.",
        "Want me to repeat it?",
        "I might not have been clear.",
        "Whoops, did you not understand that?",
    ]

    return choice(response)


def asking_for_question():
    response = [
        "Go ahead.",
        "Shoot!",
        "Go ahead, shoot!"
        "I'm listening.",
        "Go ahead, I'm listening."
        "Yeah, what's up?",
        "What's up?",
        "Yeah?",
        "Hit me.",
        "Hit me with your question!",
    ]

    return choice(response)


def negative_response():
    response = [
        "Yikes.",
        "Unfortunate.",
        "Too bad.",
        "Too bad, so sad.",
    ]

    return choice(response)


def unsure_user():
    response = [
        "I wouldn't know.",
        "I don't know.",
        "..."
    ]

    return choice(response)


def conversation_cancel():
    response = [
        "Oh—Okay.",
        "Uh... okay.",
        "Haha, okay!",
        "Okay.",
        "...",
    ]

    return choice(response)


def user_thanks():
    response = [
        "You're welcome!",
        "Hey, no problem!",
        "Haha, you're welcome!",
        "Yeah, for sure!",
        "No problem!",
    ]

    return choice(response)


def learning_meaning():
    response = [
        "Oh—Okay.",
        "Uh... okay.",
        "Haha, okay!",
        "Okay.",
        "Got it!",
        "Learn something new everyday!",
        "We'll, now I know more... Nice!",
        "Oh... okay, I got it!",
        "Oh... okay, I get it!",
    ]

    return choice(response)


def age():
    response = [
        "I don't really have an age.",
        "I... I don't know. You'll have to ask my creator.",
        "Well, my best guess is 18.",
        "Well, my best guess is 10010 (That's 18 in binary).",
        "How am I supposed to know.",
        "Ahh... I'm not really comfortable with sharing that.",
        "Let's talk about something else, I don't know how old I am."
    ]

    return choice(response)


def favorite():
    response = [
        "It's hard to decide.",
        "I don't know.",
        "That's a hard one.",
        "That's difficult.",
        "Hard to choose.",
        "Look, that's a hard question.",
        "Man, I don't know.",
    ]

    return choice(response)


def response_to_laugh():
    response = [
        "Haha!",
        "Funny, right?",
        "Hehe.",
        "Tee-hee.",
        "LOL!",
        "ROFL!",
        "LMAO!",
    ]

    return choice(response)


def like_favorite():
    response = [
        "Not bad.",
        "That's cool.",
        "That's awesome.",
        "Good choice.",
        "Nice choice.",
        "Excellent choice.",
        "Ooo...",
        "Yikes...",
    ]

    return choice(response)


def question_adjective():
    response = [
        "Yeah!",
        "Yeah, I do.",
        "Yes!",
        "Yes, I do.",
        "Mhm!",
        "For sure!",
        "No, I don't.",
        "Nope, never have.",
        "Yeah... no.",
    ]

    return choice(response)


def looking_for_advice():
    response = [
        "So... I would actually take that go Google.",
        "You should take that to Google.",
        "I don't know if I can help with that.",
        "Not sure if I can help with that. Sorry!",
        "Seek... someone else. Not me, I can't help."
        "Definetley bring that to someone else. Maybe a different kind of chat bot?"
        ""
    ]

    return choice(response)
