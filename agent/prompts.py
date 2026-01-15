def planner_prompt(user_prompt: str) -> str:
    return f"""
    you are a PLANNER agent. Convert the user prompt into a COMPLETE engeneering project plan
    user request: {user_prompt}
    """
 