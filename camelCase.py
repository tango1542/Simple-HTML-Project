#Camel Case
#Lab1
#Jeremy Wolfe

my_input_string = input('Type in a sentence: ')

words = my_input_string.split()

output_words = []

for word in words:
    output_words.append(word.lower())

for x in range(0, len(output_words)):
    if x == 0:
        my_output_string = output_words[0]
    else:
        # from https://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python
        temp = output_words[x][0].upper() + output_words[x][1:]
        my_output_string = my_output_string + temp
        temp = ''

print('Here is your string in camel case: ' + my_output_string)
