num1 = 3
string1 = 'hello '
#the code below is showing 'operator oveloading' --> this is when the same operator has differnet meaning depending on what kind of things they are applied to
num1 = num1 * 3
print(num1) #output is 9

string1 = string1 * 3
print(string1) #output is hello hello hello

word1 = 'hello'
word2 = 'world'

sentence = word1 + ' '+ word2
print(sentence)#hello world
sentence = sentence + '!'
print(sentence)


#blackjack problem
'''Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do with this type is overload the comparison operators like > and <= so that we could use them to check whether one hand beats another. e.g. it'd be cool if we could do this:

>>> hand1 = BlackjackHand(['K', 'A'])
>>> hand2 = BlackjackHand(['7', '10', 'A'])
>>> hand1 > hand2
True
Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope of these lessons), but the code we're asking you to write in the function below is very similar to what we'd have to write if we were defining our own BlackjackHand class. (We'd put it in the __gt__ magic method to define our custom behaviour for >.)'''

def calculate_total(cards):
    total = 0
    aces = 0
    for card in cards:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces +=1
        else:
            total += int(card)
    total += aces
    while aces > 0 and (total+10) <= 21 :
        total += 10
        aces = aces - 1
    return total




def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    blackjack_hand_greater_than(['K'], ['10'])
    False
    blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    if calculate_total(hand_1) <= 21 and (calculate_total(hand_2) > 21 or calculate_total(hand_1) > calculate_total(hand_2)):
        return True
    else:
        return False

print(blackjack_hand_greater_than(['K'], ['3', '4']))