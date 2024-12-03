# Specify the model
model_name = "mistralai/Mistral-7B-Instruct-v0.3"

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "left"

# Dataset formatting
def chatml_format(example):
    # Format system
    system_message = {"role": "system", "content": example['system']}
    user_message = {"role": "user", "content": example['question']}
    
    # Prompt creation
    system = tokenizer.apply_chat_template([system_message], tokenize=False) if example['system'] else ""
    prompt = tokenizer.apply_chat_template([user_message], tokenize=False, add_generation_prompt=True)
    
    # Chosen and rejected responses
    chosen = example['chosen'] + "<|im_end|>\n"
    rejected = example['rejected'] + "<|im_end|>\n"
    
    return {"prompt": system + prompt, "chosen": chosen, "rejected": rejected}

# Load dataset
dataset = load_dataset("Intel/orca_dpo_pairs")['train']

# Format dataset
formatted_dataset = dataset.map(chatml_format, remove_columns=dataset.column_names)
