def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = count_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_words} words found in the document")

    dict_letters = count_letters(text)
    list_letters = sorting_dict(dict_letters)

    for key, value in list_letters:
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

    

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    

def count_words(file_contents):
    number_words = len(file_contents.split())
    return number_words


def count_letters(text):
    dict_letters = {}

    for letter in text:
        letter_lower = letter.lower()
        if letter_lower not in dict_letters:
            dict_letters[letter_lower] = 1
        else:
            dict_letters[letter_lower] += 1
    
    return dict_letters

def sorting_dict(dict_letters):
    list_letters = list(dict_letters.items())
    list_letters.sort()

    alphabetic_letter = []

    for key, value in list_letters:
        if key.isalpha():
            alphabetic_letter.append((key, value))

    return alphabetic_letter


main()
