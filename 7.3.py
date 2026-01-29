num_to_word = {
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
}
num = input("Enter a number: ")
word_list = [num_to_word[digit] for digit in num]
word_string = ' '.join(word_list)

print("Number in words:",word_string)
