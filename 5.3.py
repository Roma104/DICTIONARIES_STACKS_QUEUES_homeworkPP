# Dictionary containing English-to-Polish translations
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

while True:
    # Prompt the user to enter a word in English
    word = input("Enter a word in English to translate (or type 'exit' to quit): ").lower()

    # Exit the program if the user types 'exit'
    if word == 'exit':
        print("Exiting the program. Goodbye!")
        break

    # Check if the word is in the dictionary and display the translation
    if word in translations:
        print(f'The Polish translation of "{word}" is "{translations[word]}".')
    else:
        print(f'Sorry, the translation for "{word}" is unavailable.')

    print()  # Add a blank line for readability
