

def main():
    with open('words_alpha.txt', 'r') as file:
        word_list = file.read().split()

    print('Enter the letters from your puzzle, separated by spaces:')
    letter_list = input().split()

    solution_words = []
    for word in word_list:
        if not (letter_list[0] in word):
            continue
        elif (len(word) < 4):
            continue

        for i, letter in enumerate(word):
            if not (letter in letter_list):
                break
            if (i == len(word) - 1):
                solution_words.append(word)

    print(str(len(solution_words)) + " words found in word list:")
    print(solution_words)


if __name__ == '__main__':
    main()

