### CREATES A PKL FILE WITH A LIST OF STRINGS (EACH STRING IS A CHAT MESSAGE).
import numpy as np
# import matplotlib.pyplot as plt
import json
import os
import pickle

# making a function for easy moving if decide to put this somewhere else
def getListOfStrings(charArray:list, data):
    for comment in data['comments']:
            message = comment['message']['body']
            chatArray.append(message)

if __name__ == '__main__': 
    # prompt user to input json file
    chatArray = list()

    while(True):
        print("filename entered will have its messages added to listOfStrings.")
        file_path = input('Enter json file path (WITH .json, enter exit to exit, enter fin when finished): ') 
        
        if type(file_path) != str: 
            print('invalid value entered, try again') 
            continue 
        elif file_path == 'exit': 
            exit(0) 
        elif file_path == 'fin':
            break
        elif not os.path.isfile(file_path): 
            print('file path entered invalid, try again') 
            continue 
        else: 
            try: 
                with open(file_path, encoding='utf-8') as f: 
                    data = json.load(f) 
            except: 
                print('file format is not correct, exiting')
                exit(0)

            # getListOfStrings
            getListOfStrings(chatArray, data)
            # print(len(chatArray))

    while(True): 
        clip_file_name = input('How do you want to name this pickle file? (WITHOUT .pkl): ') 
        if type(clip_file_name) != str: 
            print('value invalid, try again') 
            continue 
        else: 
            break 
    
    # creates folder called 'chat_words' and adds pkl to that folder
    if (not os.path.exists('chat_words')) or (not os.path.isdir('chat_words')): 
        os.makedirs('chat_words')
    with open(os.path.join('chat_words', clip_file_name + '.pkl'), 'wb') as f: 
        pickle.dump(chatArray, f)
    exit(0)
