text = input('Enter text...\n')

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)
