def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    character_dict = character_count(text.lower())
    print(sort(character_dict))


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    freq = {}
    for t in text:
        if t.isalpha():
            if t in freq:
                freq[t] += 1
            else:
                freq[t] = 1
    return freq

def sort(character_dict):
    char_list = []
    for char, num in character_dict.items():
        char_dict = {"char": char, "num": num}
        char_list.append(char_dict)
    
    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    result = ""
    for item in char_list:
        result += f"The '{item['char']}' character was found {item['num']} times\n"
    
    return result

main()