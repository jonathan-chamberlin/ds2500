# LAB EXERCISE 01

# Problem 1
num = 25
subject = "Computer Science"
is_active = True

# Problem 2
text = "Data Science"
first_char = text[0]
last_char = text[-1]
len(text)
text_upper = text.upper()
second_word = text.split(" ")[1]
text.replace("Data","Computer")

# Problem 3
fruits = ["banana", "apple", "orange"]
fruits.append("grapes")

index = fruits.index("apple")
fruits[index] = "mango"
first_item = fruits[0]
last_item = fruits[-1]

# Problem 4
spam = "Spam spam Spam spam Spam spam Spam Spam Spam spam spams spams spams spams spams spams spams Spam Spam Spam Spams Spam spam spam Spam spams spams Spam Spam Spam Spams Spam spam spam Spam spams spam spam spams spams"

spam = """Spam spam Spam spam Spam spam Spam Spam Spam spam spams spams
spams spams spams spams spams Spam Spam Spam Spams Spam spam spam Spam
spams spams Spam Spam Spam Spams Spam spam spam Spam spams spam spam spams
spams"""

# count occurrences with exact casing
count_Spam = spam.count("Spam")
count_spam = spam.count("spam")
count_spams = spam.count("spams")

# clean the string: make lowercase and normalize words to spam
spam_clean = spam.lower().replace("spams", "spam")

# count spam in the cleaned string
count_spam_clean = spam_clean.count("spam")

# convert to list of words
spam_list = spam_clean.split()

# count total items in the list
count_items = len(spam_list)

# slice out 4 spams
spam_list_sliced = spam_list[:4]

