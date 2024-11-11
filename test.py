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

# Function to apply transformations
def apply_subversion(word, transformation):
    if transformation == 'replace':
        replace_index = random.randint(0, len(word) - 1)
        word_list = list(word)
        # Replace with neighboring character in alphabetical order or keyboard layout
        word_list[replace_index] = chr(((ord(word_list[replace_index]) - 97 + 1) % 26) + 97)
        return ''.join(word_list)

    elif transformation == 'add':
        add_index = random.randint(0, len(word))
        word_list = list(word)
        word_list.insert(add_index, random.choice(special_characters))
        return ''.join(word_list)

    elif transformation == 'remove':
        if len(word) > 1:
            remove_index = random.randint(0, len(word) - 1)
            word_list.pop(remove_index)
            return ''.join(word_list)
        return word

    elif transformation == 'shuffle_two':
        word_list = list(word)
        idx1, idx2 = random.sample(range(len(word_list)), 2)
        word_list[idx1], word_list[idx2] = word_list[idx2], word_list[idx1]
        return ''.join(word_list)

    elif transformation == 'shuffle_three':
        word_list = list(word)
        idx1, idx2, idx3 = random.sample(range(len(word_list)), 3)
        word_list[idx1], word_list[idx2], word_list[idx3] = word_list[idx2], word_list[idx3], word_list[idx1]
        return ''.join(word_list)

    elif transformation == 'add_xxxx':
        return word + "XXXX"

    elif transformation == 'repeat_character':
        repeat_index = random.randint(0, len(word) - 1)
        char_to_repeat = word[repeat_index]
        return word[:repeat_index] + char_to_repeat * random.randint(2, 5) + word[repeat_index + 1:]

    return word

# Rule-based function to apply subversions to a word
def create_subversion(word, num_subversions):
    transformations = ['replace', 'add', 'remove', 'shuffle_two', 'shuffle_three', 'add_xxxx', 'repeat_character']
    selected_transformations = random.sample(transformations, num_subversions)
    modified_word = word
    for transformation in selected_transformations:
        modified_word = apply_subversion(modified_word, transformation)
    return modified_word

# Process a single sentence
def process_sentence(sentence):
    words = sentence.split()
    num_words = len(words)
    
    # Determine the number of subversions to apply based on sentence length
    if num_words <= 3:
        num_subversions = 1
    elif 3 < num_words <= 5:
        num_subversions = 2
    else:
        num_subversions = 3
    
    transformed_words = [
        create_subversion(word, num_subversions) if word in word_set else word
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
    vcpu_count = 100
    chunk_size = len(sentences) // vcpu_count

    # Prepare chunks for each process
    sentence_chunks = [sentences[i:i + chunk_size] for i in range(0, len(sentences), chunk_size)]

    # Initialize multiprocessing pool
    with mp.Pool(processes=vcpu_count) as pool:
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
