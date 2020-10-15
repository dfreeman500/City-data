import csv
from wiki import getWiki

# with open('city_data.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ')
  
#     spamwriter.writerow(['dan'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

names_of_columns = ['city','temperature', 'feels_like']

with open('city_data.csv', mode='w') as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=names_of_columns, lineterminator='\n')
    writer.writerow({'city': "Lexington"})
    # writer.writerow({'word': test_word, 'word_length_for_file': len(test_word),
    #                     'number_of_guess_for_file': len(already_guessed),
    #                     'number_of_incorrect_guesses_for_file': len(already_guessed_incorrect),
    #                     'which_dictionary_for_file': filename})