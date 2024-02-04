def replace_words(word_list):
    result_list = []

    for word in word_list:
        if len(word) > 10:
            replaced_word = word[0] + str(len(word) - 2) + word[-1]
        else:
            replaced_word = word
        result_list.append(replaced_word)

    return result_list

n = int(input())

words = [input() for _ in range(n)]

result_words = replace_words(words)
for result_word in result_words:
    print(result_word)