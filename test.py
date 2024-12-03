def chatml_format(example):
    """
    Formats a dataset example for Mistral-7B-Instruct-v0.3 using <s>[INST] [/INST] tokens.

    Args:
        example (dict): A dictionary with keys 'system', 'question', 'chosen', and 'rejected'.

    Returns:
        dict: A dictionary with 'prompt', 'chosen', and 'rejected' formatted for the model.
    """
    # Format the system message
    system_message = f"<s>[INST] {example['system']} [/INST] " if example.get('system') else ""

    # Format the user's question
    user_message = f"<s>[INST] {example['question']} [/INST] "

    # Combine system and user messages
    prompt = system_message + user_message

    # Format chosen and rejected responses
    chosen = f"{example['chosen']} </s>"
    rejected = f"{example['rejected']} </s>"

    return {
        "prompt": prompt,
        "chosen": chosen,
        "rejected": rejected,
    }
