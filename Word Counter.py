user_sentence = input("Paste a sentence or a paragraph to check its total words and vowels: ")

vowels = "aeiou"
vowel_count = 0

total_words = len(user_sentence.split())

for letter in user_sentence.lower():
    if letter in vowels:
        vowel_count += 1

print(f"Total Words: {total_words}")
print(f"Amount of Vowels Used: {vowel_count}")