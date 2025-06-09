# Write a program to create a dictionary of nepali words with values as their English 
# translation. Provide user with an option to look it up!
words={
    "kam":"work",
    "maya":"love",
    "sanchai":"fine",
    "chasma":"glass"
}
word=input("enter the word for search!")

print(words.get(word, "Word not found"))
