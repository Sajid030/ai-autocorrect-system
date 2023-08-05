# AI Autocorrect System🤖

[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white)
![Tkinter](https://img.shields.io/badge/-Tkinter-4B8BBE?logo=tkinter&logoColor=white)
![EditDistance](https://img.shields.io/badge/-EditDistance-FF6600?logo=editdistance&logoColor=white)

## Table of Contents

- [Demo](#demo)
- [Overview](#overview)
- [Features](#features)
- [Usage](#how-to-use)
- [Limitations](#limitations)

## Demo:

![GIF](resource/autocorrection.gif)

- Please consider giving a ⭐ to the repository if you find this useful.

## Overview:

The AI Autocorrect System is a Python-based application that offers real-time autocorrection suggestions to users while they type. It is designed to help users avoid spelling errors and improve the overall accuracy of their text input. The system uses statistical methods to analyze the user's input and suggest the most likely correct word based on a provided corpus.

## Features:

- **Autocorrection Suggestions:** As the user types, the application continuously monitors the input and suggests corrections for misspelled words. The autocorrection logic is based on edit distance and probability scores.

- **Edit Distance:** The system calculates the similarity between the typed word and the words in the vocabulary using edit distance. It generates candidate corrections based on single-character edits, such as insertions, deletions, substitutions, and transpositions.

- **Probability-based Scoring:** Each candidate correction is assigned a probability score based on the frequency of words in the provided text file. The system considers words with higher probabilities as better suggestions.

- **Graphical User Interface:** The application provides a user-friendly GUI developed using the Tkinter library. Users can type in the input box and receive autocorrection suggestions in real-time.

- **Selecting Suggestions:** The system displays suggestions in a list box format after waiting for 5 seconds of inactivity, allowing users to select the appropriate correction for the misspelled word. The suggestions are also ordered based on the similarity of the longer prefix, which means that similar words with longer common prefixes are suggested first in the list.

- **Automatic Word Replacement:**  If the user doesn't select from the list of autocorrection options and still the word is incorrect upon hitting the space bar, the application automatically replaces the misspelled word with the correction having the highest probability in the provided text corpus. This ensures a seamless and efficient autocorrection process without the need for explicit user selection.

## How to Use:

1. Run the application by executing the main_script.py file.
2. The GUI window will open, displaying an input box.
3. Start typing in the input box, and the application will provide real-time autocorrection suggestions.
4. If you encounter a misspelled word, the system will suggest corrections in the list box below the input box.
5. To accept a suggestion, either click on the suggested word in the list box or press the space bar.
6. The application will automatically replace the misspelled word with the selected suggestion.

Additionally some others libraries you will need to install besides python to run this application:

```bash
pip install numpy editdistance
```

## Limitations:

The current implementation of the system does not involve comprehensive linguistic analysis to understand the context or grammar of the input. Instead, it relies on statistical methods to generate suggestions based on edit distance and word probabilities.