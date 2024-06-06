# Task 1: Keyword Highlighter

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
python_reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]
for review in python_reviews: # Iterating through the list python_reviews.
    for word in keywords: # A nested for loop that iterates through the list keywords.
        if word in review: # If statement checking to see if the keyword (word) is in the review (from the list python_reviews).
            review = review.replace(word, word.upper()) # Using the .replace() function to replace each keywords with the same word in all capital letters and saving the result to a new variable. 
    print(review) # Printing our new variable.

# Task 2: Sentiment Tally

def word_count(): # Creating a new function.
    positive_count = 0 # Creating a starting count for each word list.
    negative_count = 0 # Creating a starting count for each word list.
    for words in python_reviews: # Iterating through the list python_reviews.
        for word in negative_words: # Iterating through the list negative words to find what words are found in both python_reviews and negative_words.
            if word in words: # Nested if statement checks to see if the negative word in the python_reviews list is found in the negative_words list.
                negative_count += 1 # Adding 1 to the count if the word is found in both the review (python_reviews) and the list (negative_list).
        for word in positive_words: # Iterating through the list positive words to find what words are found in both python_reviews and positive_words.
            if word in words: # Nested if statement checks to see if the positive word in the python_reviews list is found in the positive_words list.
                positive_count += 1 # Adding 1 to the count if the word is found in both the review (python_reviews) and the list (positive_list).
    print(f"Negative word count: {negative_count} \nPositive word count: {positive_count}") # Prints the string, used the f to format the string, which allows us to add the variables we've created into strings and print the result.
word_count() # Calling the function.    

# Task 3: Review Summary
def summary():
    for review in python_reviews:
        shortened_list = review[0:31] # Iterated through the first 30 characters in the list python_reviews and saves the result to a new variable called shorted_list.
        print(shortened_list + "...") # Using string concatenation to combine both the variable shortened_list with the string "..." in order to print: This product is really good. I'... The performance of this product... I had a bad experience with thi... This was a poor quality product... The product was average. Nothin...  
summary() # Calling the function.