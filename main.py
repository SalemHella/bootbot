
def words_count(text):
    words = text.split(" ")
    #print(f'word count is {len(words)}')
    wordsCount = {}
    for word in words :
        if word not in wordsCount:
            wordsCount[word] = 1
            #print(f'added {word} to the count')
        else :
            wordsCount[word] += 1
            #print(f'added one to {word} count')

    #print(f'word count is {len(words)}')
    return len(words)

def Characters_count(text):

    lower_text = text.lower()
    chars = list(lower_text)
    dic_char = {}
    for char in chars :
        if char in dic_char:
            dic_char[char] += 1
        else :
            dic_char[char] = 1

    print(dic_char)
    return dic_char

def Report(count , dict):

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count} words found in document\n')


    for key, value in dict.items()  :
        print(f'{key} character was found {value} times')

    print('--- End report ---')



path_to_file = "./books/frankenstein.txt"


with open(path_to_file) as f:

    file_contents = f.read()
    #print(file_contents)
    wordCount = words_count(file_contents)
    char_dic = Characters_count(file_contents)
    sorted_dict = dict(sorted(char_dic.items(), reverse=True, key=lambda item: item[1]))

    Report(wordCount, sorted_dict)
