def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    char_count = get_char_count(text)

    print(f"Report of {book_path}")
    print()
    print(f"Word count is: {count}")
    print()
    for values in char_count:
        print(f"The character {values} was found {char_count[values]} times.")
        

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    count = 0
    for words in text.split():
        count += 1
    return count

def get_char_count(text):
    character_counts = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1
    return character_counts    
    

    
main()