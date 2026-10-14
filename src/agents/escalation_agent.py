def escalation_agent(state):

    state["escalation"] = (
        state["sentiment"] == "negative"
    )

    return state