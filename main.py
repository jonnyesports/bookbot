def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(f"Report of {book_path}")
        
    # calculates word count
    count = 0
    for words in text.split():
        count += 1
    print(f"Word count is: {count}")
    
    # calculates character count
    character_counts = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1    
    for values in character_counts:
        print(f"The character {values} was found {character_counts[values]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()