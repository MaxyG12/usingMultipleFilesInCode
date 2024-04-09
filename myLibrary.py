#1
#import datetime
def add_diary_entry(entry_text, db):
    timestamp = datetime.datetime.now()
    db[timestamp] = entry_text
# Usage example:
# db = {}  # Initialize your database (dictionary)
# add_diary_entry("Today was a great day!", db)

#2
def get_sorted_entries(db):
  keys = db.keys()
  entry_list = sorted(keys, reverse=True)
  return [(key, db[key]) for key in entry_list]

# Usage example:
# sorted_entries = get_sorted_entries(db)
# for timestamp, entry in sorted_entries:
#     print(f"{timestamp}: {entry}")

#3
#import bcrypt

def create_hashed_password():
    # Prompt the user to create a new password
    user_password = input("Create a new password: ")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(user_password.encode(), salt)
    return hashed_password

def validate_password(hashed_password, attempts=3):
    while attempts > 0:
        user_password = input("Enter your password: ")
        if bcrypt.checkpw(user_password.encode(), hashed_password):
            print("Access granted!")
            return True
        else:
            print(f"Access denied. {attempts} attempts remaining.")
            attempts -= 1
    print("Too many incorrect attempts. Exiting.")
    return False

#if __name__ == "__main__":
    # Create and store the hashed password (you can save it in a database)
    #stored_hashed_password = create_hashed_password()

    # Validate the user-entered password
    #validate_password(stored_hashed_password)

#4
#Description: This function allows users to add a tweet to a database, associating it with a timestamp.
#Parameters: tweet (str): The tweet text to be added.
#db (dict): The database where tweets will be stored.

def add_tweet(tweet, db):
  timestamp = datetime.now()
  db[timestamp] = tweet

#Description: This function retrieves and displays tweets from the database in batches of 10, allowing the user to navigate through them.
#Parameters:
#db (dict): The database containing tweets.
def view_tweets(db):
  keys = db.keys()
  tweet_list = list(keys)
  tweet_list.reverse()

  for i in range(0, len(tweet_list), 10):
      batch = tweet_list[i:i + 10]
      for key in batch:
          print(f"{key}: {db[key]}")
          print()

      next_input = input("Next 10 tweets? (y/n) > ")
      if next_input.lower() != "y":
          break

#5
#Palindrome Checker
def palindrome(word):
  if len(word)<=1:
    return True 
    if word[0] != word[-1]:
      return False
      return palindrome(word[1:-1])

#6
#Factorial checker
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

#7





