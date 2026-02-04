"""
Python Learning App - Flask Application
A beginner-friendly web app for learning Python
"""

from flask import Flask, render_template, request, jsonify
import sys
from io import StringIO

app = Flask(__name__)

# Lesson content organized by module
LESSONS = {
    "basics": {
        "title": "Python Basics",
        "lessons": [
            {
                "id": "hello_world",
                "title": "1. Hello World",
                "description": "The one everyone starts with",
                "content": """
# This is it - your first program.
# print() shows stuff on the screen. That's it.

print("Hello, World!")
print("I just wrote my first Python program!")

# Numbers work too - no quotes needed
print(42)
print(3.14)

# Try changing the text above and hitting Run again
""",
                "exercises": [
                    {"prompt": "Print your name", "hint": 'Use print("Your Name")'},
                    {"prompt": "Print your favorite food", "hint": "Same as above, just change the text"},
                ]
            },
            {
                "id": "variables",
                "title": "2. Variables",
                "description": "Store and reuse values",
                "content": """
# Variables store values so you can use them later
# Use descriptive names that make your code readable

name = "Alice"
age = 20
gpa = 3.75
is_student = True

print("Name:", name)
print("Age:", age)
print("GPA:", gpa)

# f-strings let you embed variables directly in text
# Put an f before the quotes, then use {curly braces}
print(f"Hello {name}, you are {age} years old.")

# Variables can be updated
age = 21
print(f"After birthday: {age}")
""",
                "exercises": [
                    {"prompt": "Create a variable called 'city' with your city name and print it", "hint": "city = 'New York'"},
                    {"prompt": "Create two number variables and print their sum", "hint": "a = 5; b = 3; print(a + b)"},
                ]
            },
            {
                "id": "data_types",
                "title": "3. Data Types",
                "description": "Numbers, text, true/false - Python treats them differently",
                "content": """
# ============================================
# DATA TYPES
# ============================================
#
# Every value in Python has a type. The type determines
# what you can do with it (you can add numbers, but you
# can't add a number to a word without converting first).
#
# Main types:
#   int   - Whole numbers (42, -7, 0)
#   float - Decimal numbers (3.14, -0.5)
#   str   - Text/strings ("hello", 'world')
#   bool  - True or False (used for conditions)
#
# Use type() to check what type a value is.
# ============================================

# Integer (int) - whole numbers
count = 42
print(f"Integer: {count}, type: {type(count)}")

# Float - decimal numbers
price = 19.99
print(f"Float: {price}, type: {type(price)}")

# String (str) - text, always in quotes
message = "Hello!"
print(f"String: {message}, type: {type(message)}")

# Boolean (bool) - only True or False
is_active = True
print(f"Boolean: {is_active}, type: {type(is_active)}")

# ============================================
# TYPE CONVERSION
# ============================================
# Sometimes you need to convert between types.
# Common conversions: int(), float(), str()

age_str = "25"           # This is a string
age_num = int(age_str)   # Convert to integer
print(f"\\nConverted '{age_str}' to {age_num}")
print(f"Next year: {age_num + 1}")
""",
                "exercises": [
                    {"prompt": "Convert the string '3.14' to a float and print it", "hint": "Use float('3.14')"},
                    {"prompt": "Check the type of True using type()", "hint": "print(type(True))"},
                ]
            },
            {
                "id": "operators",
                "title": "4. Operators",
                "description": "Arithmetic and comparisons",
                "content": """
# Arithmetic operators
a = 10
b = 3

print(f"a + b = {a + b}")   # Addition
print(f"a - b = {a - b}")   # Subtraction
print(f"a * b = {a * b}")   # Multiplication
print(f"a / b = {a / b}")   # Division
print(f"a // b = {a // b}") # Floor division
print(f"a % b = {a % b}")   # Modulo (remainder)
print(f"a ** b = {a ** b}") # Exponent

# Comparison operators
x = 5
print(f"x == 5: {x == 5}")  # Equal
print(f"x != 3: {x != 3}")  # Not equal
print(f"x > 3: {x > 3}")    # Greater than
print(f"x < 10: {x < 10}")  # Less than
""",
                "exercises": [
                    {"prompt": "Check if 15 is divisible by 3 (hint: use %)", "hint": "print(15 % 3 == 0)"},
                    {"prompt": "Calculate 2 to the power of 8", "hint": "print(2 ** 8)"},
                ]
            },
            {
                "id": "input",
                "title": "5. User Input",
                "description": "Reading input from users",
                "content": """
# Note: input() is simulated in this web app
# In real Python, it pauses for user input

# input() always returns a string
name = "Alice"  # Simulating: name = input("Name: ")
print(f"Hello, {name}!")

# Convert to number for math
age_str = "20"  # Simulating: age_str = input("Age: ")
age = int(age_str)
print(f"Next year you'll be {age + 1}")

# Example calculation
score1 = 85
score2 = 90
score3 = 78
average = (score1 + score2 + score3) / 3
print(f"Average: {average:.2f}")
""",
                "exercises": [
                    {"prompt": "Calculate the average of 4 test scores: 88, 92, 79, 85", "hint": "(88 + 92 + 79 + 85) / 4"},
                    {"prompt": "Convert Fahrenheit 72 to Celsius: (F - 32) * 5/9", "hint": "print((72 - 32) * 5/9)"},
                ]
            },
        ]
    },
    "control_flow": {
        "title": "Control Flow",
        "lessons": [
            {
                "id": "if_statements",
                "title": "6. If Statements",
                "description": "Teaching your code to make decisions",
                "content": """
# ============================================
# IF STATEMENTS - Making Decisions in Code
# ============================================
#
# Programs need to make choices based on conditions.
# An if statement checks if something is True or False,
# then runs different code depending on the result.
#
# Structure:
#   if condition:
#       code to run if True
#   else:
#       code to run if False
#
# IMPORTANT: The indented code only runs when the
# condition is True. Indentation matters in Python!
# ============================================

age = 18

if age >= 18:
    print("You're an adult")
else:
    print("You're not 18 yet")

# ============================================
# ELIF - Multiple Conditions
# ============================================
# When you have more than two options, use elif
# (short for "else if"). Python checks each condition
# from top to bottom and runs the first one that's True.

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# ============================================
# COMBINING CONDITIONS
# ============================================
# Use 'and' when BOTH conditions must be True
# Use 'or' when AT LEAST ONE condition must be True
# Use 'not' to flip True to False (or vice versa)

has_ticket = True
age = 25

if age >= 18 and has_ticket:
    print("You can enter the concert")
""",
                "exercises": [
                    {"prompt": "Write code to check if a number is even or odd", "hint": "if num % 2 == 0: print('even')"},
                    {"prompt": "Check if 25 is between 10 and 50", "hint": "if 10 < 25 < 50: print('yes')"},
                ]
            },
            {
                "id": "for_loops",
                "title": "7. For Loops",
                "description": "Do something 10 times without writing it 10 times",
                "content": """
# ============================================
# FOR LOOPS - Repeating Code
# ============================================
#
# A for loop runs the same code once for each item
# in a sequence (list, string, range of numbers, etc.)
#
# Structure:
#   for variable in sequence:
#       code to repeat
#
# Each time through the loop, 'variable' takes on
# the next value from the sequence.
# ============================================

# range(start, stop) gives numbers from start to stop-1
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# ============================================
# LOOPING THROUGH LISTS
# ============================================
# The loop variable takes each item's value in order

fruits = ["apple", "banana", "cherry"]
print("\\nFruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# ============================================
# LOOPING THROUGH STRINGS
# ============================================
# Each character becomes the loop variable

print("\\nLetters in 'Python':")
for letter in "Python":
    print(letter, end=" ")
print()

# ============================================
# ACCUMULATOR PATTERN
# ============================================
# A common pattern: start with a value, then update
# it each time through the loop

total = 0
for num in range(1, 11):
    total += num  # same as: total = total + num
print(f"\\nSum of 1-10: {total}")
""",
                "exercises": [
                    {"prompt": "Print numbers 1 to 10", "hint": "for i in range(1, 11): print(i)"},
                    {"prompt": "Print the multiplication table for 5 (5x1 through 5x10)", "hint": "for i in range(1, 11): print(f'5 x {i} = {5*i}')"},
                ]
            },
            {
                "id": "while_loops",
                "title": "8. While Loops",
                "description": "Keep going until something happens",
                "content": """
# ============================================
# WHILE LOOPS - Repeat Until Done
# ============================================
#
# A while loop keeps running as long as its
# condition remains True. Use it when you don't
# know exactly how many times to repeat.
#
# Structure:
#   while condition:
#       code to repeat
#       update something so condition eventually becomes False
#
# WARNING: If the condition never becomes False,
# you get an infinite loop (the program hangs).
# ============================================

count = 5
while count > 0:
    print(count)
    count -= 1  # This ensures the loop eventually stops
print("Liftoff!")

# ============================================
# WHILE vs FOR
# ============================================
# Use FOR when you know how many times to loop
# Use WHILE when you're waiting for a condition

total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print(f"\\nSum of 1-5: {total}")

# ============================================
# BREAK AND CONTINUE
# ============================================
# break - exit the loop immediately
# continue - skip to the next iteration

print("\\nFind first even number > 10:")
n = 1
while n < 20:
    n += 1
    if n <= 10:
        continue  # Skip numbers 10 and below
    if n % 2 == 0:
        print(f"Found: {n}")
        break     # Stop once we find it
""",
                "exercises": [
                    {"prompt": "Use a while loop to print numbers 10 down to 1", "hint": "n = 10; while n > 0: print(n); n -= 1"},
                    {"prompt": "Calculate factorial of 5 (5! = 5*4*3*2*1)", "hint": "result = 1; n = 5; while n > 0: result *= n; n -= 1"},
                ]
            },
        ]
    },
    "data_structures": {
        "title": "Data Structures",
        "lessons": [
            {
                "id": "lists",
                "title": "9. Lists",
                "description": "Ordered collections of items",
                "content": """
# ============================================
# LISTS - Storing Multiple Items
# ============================================
#
# A list holds multiple values in a single variable.
# Lists are ordered (items stay in sequence) and
# mutable (you can change them after creation).
#
# Create a list with square brackets: [item1, item2, ...]
# ============================================

fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# ============================================
# INDEXING - Accessing Items
# ============================================
# Index starts at 0, not 1!
# Use negative numbers to count from the end

print(f"First item (index 0): {fruits[0]}")
print(f"Last item (index -1): {fruits[-1]}")

# ============================================
# MODIFYING LISTS
# ============================================
# Lists can grow and shrink after creation

fruits.append("date")       # Add to end
fruits.insert(1, "apricot") # Insert at specific position
print(f"After adding: {fruits}")

fruits.remove("banana")     # Remove by value
print(f"After removing: {fruits}")

# ============================================
# USEFUL LIST FUNCTIONS
# ============================================

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\\nNumbers: {numbers}")
print(f"Length: {len(numbers)}")   # How many items
print(f"Sum: {sum(numbers)}")      # Add them up
print(f"Max: {max(numbers)}")      # Largest value
print(f"Min: {min(numbers)}")      # Smallest value
print(f"Sorted: {sorted(numbers)}")# New sorted list
""",
                "exercises": [
                    {"prompt": "Create a list of 3 colors and print the second one", "hint": "colors = ['red', 'blue', 'green']; print(colors[1])"},
                    {"prompt": "Find the average of [10, 20, 30, 40, 50]", "hint": "nums = [10,20,30,40,50]; print(sum(nums)/len(nums))"},
                ]
            },
            {
                "id": "dictionaries",
                "title": "10. Dictionaries",
                "description": "Look things up by name instead of position",
                "content": """
# ============================================
# DICTIONARIES - Key-Value Storage
# ============================================
#
# A dictionary stores data as key-value pairs.
# Instead of accessing items by position (like lists),
# you access them by a unique key (usually a string).
#
# Think of it like a real dictionary:
#   word (key) -> definition (value)
#
# Create with curly braces: {key: value, key: value}
# ============================================

student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.75
}

# ============================================
# ACCESSING VALUES
# ============================================
# Use the key in square brackets to get the value

print(f"Name: {student['name']}")
print(f"GPA: {student['gpa']}")

# ============================================
# ADDING AND UPDATING
# ============================================
# Assign to a key to add or update it

student["year"] = 2      # Add new key
student["gpa"] = 3.8     # Update existing key
print(f"\\nUpdated: {student}")

# ============================================
# LOOPING THROUGH DICTIONARIES
# ============================================
# .items() gives you both keys and values

print("\\nAll student info:")
for key, value in student.items():
    print(f"  {key}: {value}")

# ============================================
# PRACTICAL EXAMPLE: COUNTING
# ============================================
# Dictionaries are great for counting occurrences

text = "the cat sat on the mat"
word_count = {}
for word in text.split():
    # .get(key, default) returns default if key doesn't exist
    word_count[word] = word_count.get(word, 0) + 1
print(f"\\nWord counts: {word_count}")
""",
                "exercises": [
                    {"prompt": "Create a dictionary for a book (title, author, year) and print the author", "hint": "book = {'title': 'Python 101', 'author': 'Jane', 'year': 2024}"},
                    {"prompt": "Count occurrences of each letter in 'hello'", "hint": "for letter in 'hello': ..."},
                ]
            },
        ]
    },
    "functions": {
        "title": "Functions",
        "lessons": [
            {
                "id": "basic_functions",
                "title": "11. Defining Functions",
                "description": "Write code once, use it forever",
                "content": """
# ============================================
# FUNCTIONS - Reusable Code Blocks
# ============================================
#
# Functions let you write code once and use it
# many times. This makes programs easier to read,
# test, and maintain.
#
# Structure:
#   def function_name(parameters):
#       code
#       return value  (optional)
#
# To use a function, "call" it by name with parentheses.
# ============================================

def greet():
    print("Hello, World!")

greet()  # Calling the function runs its code

# ============================================
# PARAMETERS - Passing Data In
# ============================================
# Parameters let you customize what the function does

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # name = "Alice"
greet_person("Bob")    # name = "Bob"

# ============================================
# RETURN VALUES - Getting Data Out
# ============================================
# Use 'return' to send a value back to the caller

def add(a, b):
    return a + b

result = add(5, 3)  # result gets the returned value
print(f"5 + 3 = {result}")

# ============================================
# DEFAULT PARAMETERS
# ============================================
# Give parameters default values for optional arguments

def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")           # Uses default "Mr."
greet_with_title("Johnson", "Dr.")  # Overrides default
""",
                "exercises": [
                    {"prompt": "Write a function that takes a number and returns its square", "hint": "def square(n): return n ** 2"},
                    {"prompt": "Write a function that checks if a number is even (returns True/False)", "hint": "def is_even(n): return n % 2 == 0"},
                ]
            },
            {
                "id": "advanced_functions",
                "title": "12. More on Functions",
                "description": "Return values, *args, and docstrings",
                "content": """
# ============================================
# MULTIPLE RETURN VALUES
# ============================================
#
# Functions can return multiple values at once.
# Python packs them into a tuple, and you can
# unpack them into separate variables.
# ============================================

def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

nums = [4, 8, 15, 16, 23, 42]
minimum, maximum, average = get_stats(nums)  # Unpacking
print(f"Min: {minimum}, Max: {maximum}, Avg: {average:.2f}")

# ============================================
# *ARGS - Variable Number of Arguments
# ============================================
#
# Use *args when you don't know how many arguments
# will be passed. They get collected into a tuple.
# ============================================

def sum_all(*numbers):
    return sum(numbers)

print(f"Sum of 3 numbers: {sum_all(1, 2, 3)}")
print(f"Sum of 5 numbers: {sum_all(1, 2, 3, 4, 5)}")

# ============================================
# DOCSTRINGS - Documenting Functions
# ============================================
#
# A docstring is a string at the start of a function
# that explains what it does. Good documentation
# helps others (and future you) understand your code.
# ============================================

def calculate_area(length, width):
    \"\"\"
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area (length * width)
    \"\"\"
    return length * width

print(f"\\nArea of 5x3 rectangle: {calculate_area(5, 3)}")

# You can access the docstring with .__doc__
print(f"\\nFunction documentation:{calculate_area.__doc__}")
""",
                "exercises": [
                    {"prompt": "Write a function that returns both the quotient and remainder of two numbers", "hint": "def divide(a, b): return a // b, a % b"},
                    {"prompt": "Write a function that takes any number of strings and joins them with spaces", "hint": "def join_words(*words): return ' '.join(words)"},
                ]
            },
        ]
    },
    "ai_fun": {
        "title": "Real AI Tools",
        "lessons": [
            {
                "id": "sentiment",
                "title": "13. Sentiment Analysis",
                "description": "Is this tweet angry or happy? Let's find out",
                "content": """
# ============================================
# SENTIMENT ANALYSIS
# ============================================
#
# What is it?
#   Sentiment analysis determines the emotional tone
#   of text - is it positive, negative, or neutral?
#
# How does it work?
#   The algorithm looks at words and phrases, comparing
#   them against a database of words labeled with their
#   typical emotional associations ("love" = positive,
#   "terrible" = negative, etc.)
#
# Real-world uses:
#   - Analyzing customer reviews
#   - Monitoring social media mentions
#   - Measuring public opinion
#
# We're using TextBlob, a Python library that makes
# natural language processing simple.
# ============================================

from textblob import TextBlob

def analyze_feeling(text):
    blob = TextBlob(text)

    # Polarity ranges from -1.0 (very negative) to +1.0 (very positive)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        mood = "POSITIVE"
    elif polarity < -0.1:
        mood = "NEGATIVE"
    else:
        mood = "NEUTRAL"

    return mood, polarity

# Test sentences
sentences = [
    "I love this class! Python is amazing!",
    "This homework is terrible and boring.",
    "The weather is cloudy today.",
    "Best pizza I've ever had!",
    "I'm so frustrated with this error.",
    "The meeting is at 3pm.",
]

print("Sentiment Analysis Results")
print("-" * 40)

for sentence in sentences:
    mood, score = analyze_feeling(sentence)
    print(f'"{sentence}"')
    print(f"  -> {mood} (score: {score:.2f})")
    print()
""",
                "exercises": [
                    {"prompt": "Analyze your own sentence - what mood does it detect?", "hint": "Add your sentence to the sentences list"},
                    {"prompt": "Try a sarcastic sentence - does the AI understand sarcasm?", "hint": 'Try something like "Oh great, another Monday"'},
                ]
            },
            {
                "id": "spam_detector",
                "title": "14. Spam Detector AI",
                "description": "Train your own \"is this spam?\" detector",
                "content": """
# ============================================
# SPAM DETECTION WITH MACHINE LEARNING
# ============================================
#
# What is Machine Learning?
#   Instead of writing rules by hand ("if email contains
#   'FREE', mark as spam"), we show the computer examples
#   and let it learn the patterns itself.
#
# How this works:
#   1. TRAINING: Give the model labeled examples
#      (emails we've already marked as spam or not spam)
#   2. LEARNING: The model finds patterns in the data
#      (spam emails often have certain words)
#   3. PREDICTING: Given a new email, the model uses
#      those patterns to make a prediction
#
# We're using:
#   - CountVectorizer: Converts text to numbers by
#     counting how often each word appears
#   - MultinomialNB: Naive Bayes classifier, a simple
#     but effective algorithm for text classification
# ============================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# STEP 1: Training data (examples with labels)
training_emails = [
    "Congratulations! You won a free iPhone!",
    "URGENT: Claim your prize money now!!!",
    "Get rich quick! Make $1000 daily!",
    "FREE FREE FREE click here now",
    "You have been selected as a winner!",
    "Hey, are we still meeting for lunch?",
    "The project deadline is next Friday",
    "Can you send me the meeting notes?",
    "Happy birthday! Hope you have a great day",
    "Your Amazon order has shipped",
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1=spam, 0=not spam

# STEP 2: Convert text to numbers and train
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_emails)

model = MultinomialNB()
model.fit(X_train, labels)

print(f"Model trained on {len(training_emails)} examples")
print()

# STEP 3: Test on new emails
test_emails = [
    "FREE money!!! Click here to claim your prize!",
    "Hey, want to grab coffee tomorrow?",
    "You WON $1,000,000 dollars!!!",
    "The homework is due on Monday",
    "URGENT WINNER SELECTED FREE GIFT",
]

print("Predictions on new emails:")
print("-" * 40)

for email in test_emails:
    X_test = vectorizer.transform([email])
    prediction = model.predict(X_test)[0]
    confidence = max(model.predict_proba(X_test)[0]) * 100

    result = "SPAM" if prediction == 1 else "NOT SPAM"
    print(f'"{email[:35]}..."')
    print(f"  -> {result} ({confidence:.0f}% confidence)")
    print()
""",
                "exercises": [
                    {"prompt": "Add more training examples to improve accuracy", "hint": "Add more spam and non-spam emails to the lists"},
                    {"prompt": "Test an email you've received - is it spam?", "hint": "Add your email text to test_emails"},
                ]
            },
            {
                "id": "text_features",
                "title": "15. AI Text Analysis",
                "description": "Pull out names, topics, and stats from any text",
                "content": """
# ============================================
# TEXT ANALYSIS - Extracting Information
# ============================================
#
# What is NLP (Natural Language Processing)?
#   NLP is a field of AI that helps computers understand
#   human language. It powers search engines, voice
#   assistants, and translation services.
#
# Part-of-Speech Tagging:
#   The computer identifies each word's role in a sentence:
#   - NN = Noun (person, place, thing)
#   - NNP = Proper Noun (specific name)
#   - VB = Verb (action word)
#   - JJ = Adjective (describes a noun)
#
# Noun Phrase Extraction:
#   Finds meaningful phrases that represent key topics
#   (e.g., "programming language", "machine learning")
# ============================================

from textblob import TextBlob

text = \"\"\"
Python is a popular programming language. It was created by
Guido van Rossum in the Netherlands. Many companies like
Google, Netflix, and Instagram use Python. Students love
learning Python because it is easy and powerful.
\"\"\"

# Create a TextBlob object to analyze the text
blob = TextBlob(text)

# Extract key topics (noun phrases)
print("KEY TOPICS FOUND:")
for phrase in blob.noun_phrases:
    print(f"  - {phrase}")

print()

# Basic statistics
print("TEXT STATISTICS:")
print(f"  Words: {len(blob.words)}")
print(f"  Sentences: {len(blob.sentences)}")

print()

# Part-of-speech tagging - find all nouns
print("NOUNS IN THE TEXT:")
nouns = [word for word, tag in blob.tags if tag in ('NN', 'NNP')]
print(f"  {', '.join(set(nouns))}")

print()

# Find all verbs
print("VERBS IN THE TEXT:")
verbs = [word for word, tag in blob.tags if tag.startswith('VB')]
print(f"  {', '.join(set(verbs))}")
""",
                "exercises": [
                    {"prompt": "Analyze a paragraph from your favorite book or article", "hint": "Replace the text variable with your own text"},
                    {"prompt": "Count how many times a specific word appears", "hint": "Use blob.words.count('word')"},
                ]
            },
            {
                "id": "movie_recommender",
                "title": "16. Movie Recommender AI",
                "description": "\"If you liked X, try Y\" - how Netflix does it",
                "content": """
# ============================================
# RECOMMENDATION SYSTEMS
# ============================================
#
# How do Netflix, Spotify, and Amazon know what to suggest?
# There are two main approaches:
#
# 1. CONTENT-BASED FILTERING (what we're building):
#    - Compare item descriptions/features
#    - "You liked action movies, here are more action movies"
#
# 2. COLLABORATIVE FILTERING:
#    - Compare user behavior
#    - "Users similar to you also liked..."
#
# Key Concepts:
#   TF-IDF (Term Frequency-Inverse Document Frequency):
#     Converts text to numbers, giving more weight to
#     distinctive words and less to common ones.
#
#   COSINE SIMILARITY:
#     Measures how similar two vectors are (0 to 1).
#     1.0 = identical, 0.0 = completely different
# ============================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Our movie database - each movie has descriptive keywords
movies = {
    "The Matrix": "sci-fi action hacker computer virtual reality martial arts",
    "John Wick": "action assassin revenge guns martial arts dog",
    "Inception": "sci-fi dreams heist mind thriller action",
    "The Notebook": "romance love drama tears emotional relationship",
    "Titanic": "romance drama ship ocean love tragedy historical",
    "Avengers": "superhero action marvel team fighting aliens",
    "Iron Man": "superhero action marvel technology genius robot",
    "Finding Nemo": "animation fish ocean family adventure kids",
    "Toy Story": "animation toys friendship adventure kids family",
    "The Godfather": "crime drama mafia family power revenge",
}

# Step 1: Convert text descriptions to numerical vectors
vectorizer = TfidfVectorizer()
movie_names = list(movies.keys())
movie_vectors = vectorizer.fit_transform(movies.values())

def recommend(movie_name, num_recs=3):
    if movie_name not in movies:
        return []

    # Step 2: Find the movie's vector
    idx = movie_names.index(movie_name)

    # Step 3: Calculate similarity to all other movies
    similarities = cosine_similarity(movie_vectors[idx], movie_vectors)[0]

    # Step 4: Return the most similar (excluding itself)
    top_indices = similarities.argsort()[::-1][1:num_recs+1]
    return [(movie_names[i], similarities[i]) for i in top_indices]

# Test the recommender
print("MOVIE RECOMMENDATIONS")
print("=" * 40)

for movie in ["The Matrix", "The Notebook", "Finding Nemo"]:
    print(f"\\nIf you liked '{movie}':")
    for rec, score in recommend(movie):
        print(f"  -> {rec} ({score:.0%} similar)")
    print()
""",
                "exercises": [
                    {"prompt": "Add your favorite movie to the database", "hint": "Add a new entry with keywords describing the movie"},
                    {"prompt": "Change num_recommendations to 5 to see more suggestions", "hint": "recommend(movie, num_recommendations=5)"},
                ]
            },
        ]
    }
}


@app.route('/')
def index():
    """Home page with lesson overview"""
    return render_template('index.html', lessons=LESSONS)


@app.route('/lesson/<module>/<lesson_id>')
def lesson(module, lesson_id):
    """Display a specific lesson"""
    if module not in LESSONS:
        return "Module not found", 404

    module_data = LESSONS[module]
    lesson_data = None
    for l in module_data['lessons']:
        if l['id'] == lesson_id:
            lesson_data = l
            break

    if not lesson_data:
        return "Lesson not found", 404

    return render_template('lesson.html',
                          module=module,
                          module_title=module_data['title'],
                          lesson=lesson_data,
                          all_lessons=LESSONS)


@app.route('/run', methods=['POST'])
def run_code():
    """Execute Python code and return output"""
    code = request.json.get('code', '')

    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    output = ""
    error = ""

    try:
        # Execute the code
        exec(code, {"__builtins__": __builtins__})
        output = sys.stdout.getvalue()
    except Exception as e:
        error = f"{type(e).__name__}: {str(e)}"
    finally:
        sys.stdout = old_stdout

    return jsonify({
        'output': output,
        'error': error
    })


@app.route('/reference')
def reference():
    """Quick reference page"""
    return render_template('reference.html')


if __name__ == '__main__':
    import os
    # Use 0.0.0.0 in containers, 127.0.0.1 locally
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'true').lower() == 'true'
    app.run(host=host, port=port, debug=debug)
