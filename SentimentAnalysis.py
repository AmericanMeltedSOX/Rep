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

#   Negative LIST
def negative_comments_list(comment):
    list = []
    #Initializes empty list and checks for sentiment scores

    meter2 = get_text_negative_proba(comment.body)
    meter1 = get_text_positive_proba(comment.body)
    meter3 = get_text_neutral_proba(comment.body)

    """If the comment holds true to this condition, the comment is
    then added to the list."""
    if meter2 > meter1 and meter2 > meter3:
        list.append(comment)

    #Recursive process; the parent comment's replies are passed through this same method.
    for i in range(len(comment.replies)):
        list += negative_comments_list(comment.replies[i])

    return list

#   Positive LIST
def positive_comments_list(comment):
    list = []
    #Initializes empty list and checks for sentiment scores

    meter1 = get_text_positive_proba(comment.body)
    meter2 = get_text_negative_proba(comment.body)
    meter3 = get_text_neutral_proba(comment.body)

    """If the comment holds true to this condition, the comment is
    then added to the list."""
    if meter1 > meter2 and meter1 > meter3:
        list.append(comment)

    #Recursive process; the parent comment's replies are passed through this same method.
    for i in range(len(comment.replies)):
        list += positive_comments_list(comment.replies[i])

    return list

#   Neutral LIST
def neutral_comments_list(comment):
    list = []
    #Initializes empty list and checks for sentiment scores

    meter3 = get_text_neutral_proba(comment.body)
    meter2 = get_text_negative_proba(comment.body)
    meter1 = get_text_positive_proba(comment.body)

    """If the comment holds true to this condition, the comment is
    then added to the list."""
    if(meter3 > meter1 and meter3 > meter2):
        list.append(comment)

    #Recursive process; the parent comment's replies are passed through this same method.
    for i in range(len(comment.replies)):
        list += neutral_comments_list(comment.replies[i])

    return list


#   PRINTS LIST
def print_list(list):
    try:
        if not list:    #Checks for empty list
            return None

        comment = list.pop()

        #Checks for sentiment scores
        positive = get_text_positive_proba(comment.body)
        negative = get_text_negative_proba(comment.body)
        neutral = get_text_neutral_proba(comment.body)

        #Print operaions
        print("'", comment.body, "'")
        print("Positive Sentiment: ", positive)
        print("Negative Sentiment: ", negative)
        print("Neutral Sentiment: ", neutral)
        print("")

        print_list(list)

    except RecursionError:
        print("Error: Check for any index error. Index value might be repeating itself.")
        return None

def main():
    try:
        comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')

        print(len(comments))

        #NOTE: For loops are used to pass every root comment individually. If the user simply wants a list
        #      of replies within a root comment the range values have to modified to acommodate the length/
        #      number of replies.
        print("NEGATIVE POSTS:")
        neg_list = []

        for i in range(len(comments)):
            neg_list += negative_comments_list(comments[i])

        neg_list.reverse()
        print_list(neg_list)

        print("")
        print("POSITIVE POSTS: ")
        pos_list = []

        for i in range(len(comments)):
            pos_list += positive_comments_list(comments[i])

        pos_list.reverse()
        print_list(pos_list)

        print("")
        print("NEUTRAL POSTS: ")
        neut_list = []

        for i in range(len(comments)):
            neut_list += neutral_comments_list(comments[i])

        neut_list.reverse()
        print_list(neut_list)

    except IndexError:
        print("Error: Check Your Indexes and Range.")
    except TypeError:
        print("Error: Check that Range is actually an integer.")



main()
