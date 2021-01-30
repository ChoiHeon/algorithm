def match(wild_card, words):
    match_words = []
    len_wild_card = len(wild_card)

    for word in words:
        len_word = len(word)
        path = [[False] * (len_wild_card + 1) for i in range(len_word + 1)]
        path[0][0] = True

        for i in range(len_word):
            for j in range(len_wild_card):
                if path[i][j]:
                    if wild_card[j] == '*':
                        path[i + 1][j] = True
                        path[i][j + 1] = True
                    elif wild_card[j] == '?' or wild_card[j] == word[i]:
                        path[i + 1][j + 1] = True
                    else:
                        path[i][j] = False

                    if path[i][j] and j < len_wild_card - 1 and wild_card[j + 1] == '*':
                        path[i][j + 1] = True

        if path[len_word - 1][len_wild_card - 1]:
            match_words.append(word)

    match_words.sort()
    for word in match_words:
        print(word)


# main
# input case repeat count
count = int(input())

while count > 0:
    # input wild card
    wild_card = input()

    # word count
    word_count = int(input())

    # input words
    words = []
    for i in range(0, word_count):
        words.append(input())

    match(wild_card, words)

    count -= 1