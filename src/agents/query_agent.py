def query_agent(state):

    query = state["query"].lower()

    if "refund" in query:
        state["intent"] = "refund"

    elif "password" in query:
        state["intent"] = "password"

    elif "delivery" in query:
        state["intent"] = "delivery"

    elif "loan" in query:
        state["intent"] = "loan"

    else:
        state["intent"] = "general"

    return state