import tkinter as tk
import numpy as np
from autocorrect_package.autocorrection import Autocorrection

class AutoCorrectApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize the Autocorrection object with the desired file
        self.checker = Autocorrection("autocorrect_package/corpus.txt")

        # Create an input box(Text widget) for the user to type
        self.input_box = tk.Text(self, wrap="word")
        self.input_box.pack()

        # Creating a Listbox widget to display suggestions
        self.suggestion_listbox = tk.Listbox(self)
        self.suggestion_listbox.pack()

        # Bind the key release event to call the on_key_release method
        self.input_box.bind("<KeyRelease>", self.on_key_release)

        # Bind the space bar event to call the on_space_bar_press method
        self.input_box.bind("<space>", self.on_space_bar_press)
        
        # Bind the listbox select event to call the on_listbox_select method
        self.suggestion_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

        # Initialize a variable to store the current word being typed
        self.current_word = ""

    def on_key_release(self, event):
        # Get the current position of the cursor(insertion point)
        cursor_position = self.input_box.index(tk.INSERT)

        # Get the word currently being typed by the user
        current_line = self.input_box.get("insert linestart", cursor_position).split()
        self.current_word = current_line[-1]

        # Wait for 2 seconds of inactivity(no key presses) before suggesting autocorrections
        self.after(2000, self.autocorrect_suggestions)

    def on_space_bar_press(self, event):
        # Check if any suggestion was selected from the suggestion box
        if self.suggestion_listbox.curselection():
            return

        # If no suggestion is selected, proceed with autocorrection logic

        # Get the current word being typed by the user
        word = self.current_word.lower()

        # Perform the autocorrection logic using the Autocorrection class
        corrections = self.checker.correct_spelling(word)

        # Get the word with the highest probability from the corrections list
        if corrections:
            probs = np.array([c[1] for c in corrections])
            best_ix = np.argmax(probs)
            correct = corrections[best_ix][0]

            highest_prob_word = correct

            # Replace the wrong word with the word with the highest probability
            if highest_prob_word != word:
                self.input_box.delete(f"insert-{len(word)}c", "insert")
                self.input_box.insert("insert", highest_prob_word + "")

            print(f"Did you mean {highest_prob_word}?")


    def autocorrect_suggestions(self):
        # Get the current word being typed by the user
        word = self.current_word.lower()

        # Perform the autocorrection logic using the Autocorrection class
        corrections = self.checker.correct_spelling(word)

        # Clear the existing suggestions from the listbox
        self.suggestion_listbox.delete(0, tk.END)

        # Show the suggestions in the listbox
        if corrections:
            for correction in corrections:
                self.suggestion_listbox.insert(tk.END, correction[0])
    
    def on_listbox_select(self, event):
        # Get the selected word from the listbox
        selected_word = self.suggestion_listbox.get(self.suggestion_listbox.curselection())

        # Replace the current word in the input box with the selected word
        self.input_box.delete(f"insert-{len(self.current_word)}c", "insert")
        self.input_box.insert("insert", selected_word + " ")

        # Clear the existing suggestions from the listbox after selecting one
        self.suggestion_listbox.delete(0, tk.END)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = AutoCorrectApp()
    app.run()
