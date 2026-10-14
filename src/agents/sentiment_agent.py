def sentiment_agent(state):

    query = state["query"].lower()

    negative_words = [
        "angry",
        "worst",
        "bad",
        "complaint",
        "frustrated"
    ]

    if any(word in query for word in negative_words):
        state["sentiment"] = "negative"
    else:
        state["sentiment"] = "neutral"

    return state