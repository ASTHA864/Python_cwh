# Q7. Write a function to remove a given word from a list and strip it at the same time.

def remove_and_strip(word_list, word_to_remove):
    # Strip whitespace from each element and remove the given word
    return [word.strip() for word in word_list if word.strip() != word_to_remove]

# Example usage
words = ["  apple  ", "banana", "  cherry  ", "apple", "  date  "]
word_to_remove = "apple"
result = remove_and_strip(words, word_to_remove)
print(result)  # Output: ['banana', 'cherry', 'date']