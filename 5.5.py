# Paragraph to analyze
paragraph = "cat dog mouse cat rat cat mouse"

# Split the paragraph into words
words = paragraph.split()

# Dictionary to store the word count
word_count = {}

# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the result
for word, count in word_count.items():
    print(f"{word}: {count}")
