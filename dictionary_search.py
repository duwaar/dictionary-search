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

    def remove_markers(self, word):
        while (not word.isalpha() and len(word) > 0):
            word = word[:-1]
        return word

    def on_search_button_pressed(self):
        required_letters = self.required_letter_selector.GetCheckedStrings()

        source_letters = self.source_letter_selector.GetCheckedStrings()
        for letter in required_letters:
            source_letters.append(letter)

        dictionary_path = os.path.join(os.sep,
                os.getcwd(),
                'dictionaries',
                self.dictionary_selector.GetStringSelection()
                )
        with open(dictionary_path) as file:
            word_list = file.read().split()

        found_words = ''
        for word in word_list:
            word = self.remove_markers(word)
            if (self.all_A_in_B(required_letters, word)
                    and self.all_A_in_B(word, source_letters)
                    ):
                found_words = found_words + word + '\n'
        
        self.found_words_box.SetValue(found_words)



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

