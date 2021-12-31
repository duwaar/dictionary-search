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

        self.dictionaries = os.listdir('dictionaries')
        print(self.dictionaries)

    def on_search_button_pressed(self):
        print('No function implemented for "on_search_button_pressed"')

class DictionarySearchApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

def main():
    app = DictionarySearchApp(0)
    app.MainLoop()


if __name__ == '__main__':
    main()

