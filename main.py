def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    ordered_list = dict_to_list(get_nb_char(text))
    ordered_list.sort(reverse=True, key=sort_on)
    print (ordered_list)
    for elem in ordered_list:
        print (f"The '{elem["char"]}' character was found {elem["count"]} times") 


def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_nb_char(text):
    dic_char = {}
    for char in text:
        if char.lower() in dic_char:
            dic_char[char.lower()] += 1
        else:
            dic_char[char.lower()] = 1
    return(dic_char)


def dict_to_list(dict):
    list_dict = []
    for x in dict:
        if (x.isalpha()):
            list_dict.append({"char":x,"count":dict[x]})
    return list_dict

    
main()
