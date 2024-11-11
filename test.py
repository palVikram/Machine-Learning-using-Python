import random
import string
import multiprocessing as mp
import pickle
import os

# Define your dictionary as a set for efficient lookups
word_dictionary = {"example", "dictionary", "words", "for", "subversion"}  # Add your dictionary words here
word_set = set(word_dictionary)  # Convert to set for fast lookup
sentences = ["This is an example sentence", "Another dictionary sentence with words"]  # Add your sentences list here

# Define the special characters pool
special_characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:'\",.<>?/~`"

# Function to apply a single transformation
def apply_subversion(word, transformation):
    word_list = list(word)  # Initialize word_list from word at the beginning

    if transformation == 'replace':
        replace_index = random.randint(0, len(word_list) - 1)
        # Replace with a random special character
        word_list[replace_index] = random.choice(special_characters)
        return ''.join(word_list)

    elif transformation == 'add':
        add_index = random.randint(0, len(word_list))
        # Add a random special character at a random position
        word_list.insert(add_index, random.choice(special_characters))
        return ''.join(word_list)

    elif transformation == 'remove':
        if len(word_list) > 1:  # Check to avoid empty list error
            remove_index = random.randint(0, len(word_list) - 1)
            word_list.pop(remove_index)
        return ''.join(word_list)

    elif transformation == 'shuffle_two':
        if len(word_list) >= 2:
            idx1, idx2 = random.sample(range(len(word_list)), 2)
            word_list[idx1], word_list[idx2] = word_list[idx2], word_list[idx1]
        return ''.join(word_list)

    elif transformation == 'shuffle_three':
        if len(word_list) >= 3:
            idx1, idx2, idx3 = random.sample(range(len(word_list)), 3)
            word_list[idx1], word_list[idx2], word_list[idx3] = word_list[idx2], word_list[idx3], word_list[idx1]
        return ''.join(word_list)

    elif transformation == 'add_xxxx':
        return word + "XXXX"

    elif transformation == 'repeat_character':
        repeat_index = random.randint(0, len(word_list) - 1)
        char_to_repeat = word_list[repeat_index]
        return ''.join(word_list[:repeat_index] + [char_to_repeat * random.randint(2, 5)] + word_list[repeat_index + 1:])

    return word

# Function to apply a single random subversion to a word
def create_subversion(word):
    transformations = ['replace', 'add', 'remove', 'shuffle_two', 'shuffle_three', 'add_xxxx', 'repeat_character']
    selected_transformation = random.choice(transformations)
    return apply_subversion(word, selected_transformation)

# Process a single sentence with only one transformation per word
def process_sentence(sentence):
    words = sentence.split()
    
    transformed_words = [
        create_subversion(word) if word in word_set else word
        for word in words
    ]
    return ' '.join(transformed_words)

# Save results to a file
def save_to_file(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

# Multiprocessing handler
def process_sentences(sentences, start_index):
    result = []
    cumulative_results = []
    for i, sentence in enumerate(sentences):
        transformed_sentence = process_sentence(sentence)
        result.append(transformed_sentence)
        cumulative_results.append(transformed_sentence)

        # Save every 100 sentences processed
        if (start_index + i + 1) % 100 == 0:
            save_to_file(result, f"processed_sentences_{start_index + i + 1}.pkl")
            print(f"Saved file for sentences {start_index + i + 1}")

            # Every additional 100 sentences, save cumulative results
            if (start_index + i + 1) % 200 == 0:
                save_to_file(cumulative_results, "cumulative_results.pkl")
                print(f"Saved cumulative results up to sentence {start_index + i + 1}")

            # Clear the result list after saving to start fresh for the next 100
            result.clear()

    return cumulative_results

def main():
    # Number of vCPUs available
    vcpu_count = os.cpu_count() or 100  # Fallback to 100 if os.cpu_count() returns None
    chunk_size = max(1, len(sentences) // vcpu_count)  # Ensure chunk_size is at least 1

    # Prepare chunks for each process
    sentence_chunks = [sentences[i:i + chunk_size] for i in range(0, len(sentences), chunk_size)]

    # Limit the number of processes to the number of chunks
    process_count = min(vcpu_count, len(sentence_chunks))

    # Initialize multiprocessing pool
    with mp.Pool(processes=process_count) as pool:
        results = pool.starmap(process_sentences, [(chunk, i * chunk_size) for i, chunk in enumerate(sentence_chunks)])

    # Flatten the list of results
    transformed_sentences = [sentence for sublist in results for sentence in sublist]
    print("All sentences processed.")
    return transformed_sentences

# Run the main function
if __name__ == "__main__":
    transformed_sentences = main()
    # Save the final set of transformed sentences if needed
    save_to_file(transformed_sentences, "final_transformed_sentences.pkl")
    print("Final transformed sentences saved.")
