"""
CS 2302: LAB 1 Option B
From: ISAAC ACOSTA
DATE: 9/12/18
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='BtG-jWLucK3zOQ',
                     client_secret='8veQJFmbaLELdZFwL1u9gIvFatU',
                     user_agent='MeltedSOX'
                     )


#nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']

def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']

def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']

def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments

  
#   LIST GENREATOR RECURSIVELY
def get_list(comment, x, y, z):
    list = []
    #Initializes empty list and checks for sentiment scores

    meter = [get_text_negative_proba(comment.body), get_text_positive_proba(comment.body), get_text_neutral_proba(comment.body)]

    """If the comment holds true to this condition, the comment is
    then added to the list."""
    if meter[x] > meter[y] and meter[x] > meter[z]:
        list.append(comment)

    #Recursive process; the parent comment's replies are passed through this same method.
    for i in range(len(comment.replies)):
        list += get_list(comment.replies[i], x, y, z)

    return list


"""   --------PRINTS LIST--------"""
def print_list(list, x, n):
    try:
        if not list:    #Checks for empty list
            return None
        #Checks if list will be Negative, Positive, or Neutral
        if x == 0:
            print("NEGATIVE COMMENTS: ")
        if x == 1:
            print("POSITIVE COMMENTS: ")
        if x == 2:
            print("NEUTRAL COMMENTS: ")

        comment = list.pop()

        #Print operaion
        ## 'n' is used as a counter to number list when printing
        print(n, '. ', comment.body, "'")
        print("")
        print_list(list, -1, n+1)

    except RecursionError:
        print("Error: Check for any index error. Index value might be repeating itself.")
        return None

def main():
    try:
        comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')

        """NOTE: Top level comments are passed into the recursive method that outputs the list.
                This is necessary in order to traverse the complete list of comments and replies.
        """

        ##Gets lst for negative comments
        negative_comments_list = []
        for top_level_comment in comments:
            negative_comments_list += get_list(top_level_comment, 0, 1, 2)

        negative_comments_list.reverse()

        ##Gets list for positive comments
        positive_comments_list = []
        for top_level_comment in comments:
            positive_comments_list += get_list(top_level_comment, 1, 0, 2)

        positive_comments_list.reverse()

        ##Gets lst for neutral comments
        neutral_comments_list = []
        for top_level_comment in comments:
            neutral_comments_list += get_list(top_level_comment, 2, 1, 0)

        neutral_comments_list.reverse()
        #print_list(neutral_comments_list, 2)


        """PRINT LIST OPTION"""
        ans = (input("Do you wish to print the three list? Y/N "))
        if ans == "Y" or ans == "y":
            print_list(negative_comments_list, 0, 1)
            print_list(positive_comments_list, 1, 1)
            print_list(neutral_comments_list, 2, 1)
        else:
            print("exit")

    except IndexError:
        print("Error: Check Your Indexes and Range.")
    except TypeError:
        print("Error: Check that Range is actually an integer.")


main()
