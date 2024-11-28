from transformers import AutoTokenizer

# Load the tokenizer for Mistral v0.3
model_id = "mistralai/Mistral-7B-v0.3"
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Ensure pad_token_id is set
if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

# Verify the tokenizer's maximum supported length
print(f"Tokenizer maximum length: {tokenizer.model_max_length}")  # Should be 32768

# Define the chat template
DEFAULT_CHAT_TEMPLATE = """
{% for message in messages %}
    {% if message['role'] == 'user' %}
        {{ '<|user|>\n' + message['content'] + eos_token }}
    {% elif message['role'] == 'system' %}
        {{ '<|system|>\n' + message['content'] + eos_token }}
    {% elif message['role'] == 'assistant' %}
        {{ '<|assistant|>\n' + message['content'] + eos_token }}
    {% endif %}
    {% if loop.last and add_generation_prompt %}
        {{ '<|assistant|>' }}
    {% endif %}
{% endfor %}
"""
# Attach the chat template to the tokenizer
tokenizer.chat_template = DEFAULT_CHAT_TEMPLATE

# Function to apply the chat template
def apply_chat_template(example, tokenizer):
    messages = example["messages"]
    # Ensure a system message is present
    if messages[0]["role"] != "system":
        messages.insert(0, {"role": "system", "content": ""})
    # Apply the chat template from the tokenizer
    example["text"] = tokenizer.apply_chat_template(messages, tokenize=False)
    return example

# Map the dataset with the updated chat template
from multiprocessing import cpu_count
raw_datasets = raw_datasets.map(
    apply_chat_template,
    num_proc=cpu_count(),
    fn_kwargs={"tokenizer": tokenizer},
    remove_columns=list(raw_datasets["train"].features),
    desc="Applying chat template",
)

# Create training and evaluation splits
train_dataset = raw_datasets["train"]
eval_dataset = raw_datasets["test"]

# Debug: Print a few samples to verify tokenization and formatting
import random
for index in random.sample(range(len(raw_datasets["train"])), 3):
    print(f"Sample {index} of the processed training set:\n\n{raw_datasets['train'][index]['text']}")
