

def main():
    with open('words_alpha.txt', 'r') as file:
        word_list = file.read().split()

    with open('letters.txt', 'r') as file:
        letter_list = file.read().split()

    with open('solution_words.txt', 'w') as solutions_file:
        solution_count = 0
        for word in word_list:
            if not (letter_list[0] in word):
                continue
            elif (len(word) < 4):
                continue

            for i, letter in enumerate(word):
                if not (letter in letter_list):
                    break
                if (i == len(word) - 1):
                    solutions_file.write(word + '\n')
                    solution_count += 1

        print(str(solution_count) + " words found in word list.")


if __name__ == '__main__':
    main()

