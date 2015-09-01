string ="Hola soy una cadena de texto extremadamente larga"
string_list = string.lower().split()
string_dict = {}

def word_count(word):
    for word in string_list:
        if word in string_dict:
            string_dict[word] = string_dict[word] + 1
            continue
        else:
            string_dict[word] = 1

    return string_dict

dict = word_count(string)
print(dict)
