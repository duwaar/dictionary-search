import wx, os
import dictionary_search_gui as gui


'''
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
'''



class MyFrame(gui.SearchFrame):
    def __init__(self, *args, **kwds):
        gui.SearchFrame.__init__(self, *args, **kwds)
        self.dictionary_selector.Set(os.listdir('dictionaries'))
        self.dictionary_selector.SetSelection(0)

        with open('README.md', 'r') as file:
            self.help_box.SetValue(file.read())

    def all_A_in_B(self, A, B):
        set_A = set(A)
        set_B = set(B)
        elements_in_common = set_A.intersection(set_B)
        return len(elements_in_common) == len(set_A)

    def strip_word(self, word):
        stripped_word = word.strip()
        if (stripped_word.isalpha()):
            return stripped_word
        else:
            clean_word = ''
            for character in stripped_word:
                if (character.isalpha()):
                    clean_word = clean_word + character
            return clean_word

    def on_search_button_pressed(self):
        required_letters = self.required_letter_selector.GetCheckedStrings()

        source_letters = self.source_letter_selector.GetCheckedStrings()

        # This should be refactored into a load_dictionary() function, or something.
        dictionary_path = os.path.join(os.sep,
                os.getcwd(),
                'dictionaries',
                self.dictionary_selector.GetStringSelection()
                )
        with open(dictionary_path) as file:
            word_list = file.read().split()

        # This should be refactored into a find_words() function, or something.
        found_words = []
        for word in word_list:
            # Cleaning the words should be done earlier--when the word list is loaded.
            clean_word = self.strip_word(word)
            if (not clean_word):
                continue
            # Dear God. I hope this if-statement can be made cleaner.
            if (self.all_A_in_B(required_letters, clean_word)
                    and (self.all_A_in_B(clean_word, source_letters)
                    or self.all_A_in_B(clean_word, required_letters))
                    ):
                found_words.append(clean_word)
        
        found_words_string = ''
        for word in found_words:
            found_words_string += word + '\n'
        self.found_words_box.SetValue(found_words_string)
        self.word_count_box.SetValue(str(len(found_words)))




class DictionarySearchApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, '')
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

def main():
    app = DictionarySearchApp(0)
    app.MainLoop()


if __name__ == '__main__':
    main()

