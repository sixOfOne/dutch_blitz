# Input player names :: player_name[i] 
while True:
    print('Please type your name.')
    name = input('>')
    if name == 'your name':
        break
print('Thank you!')
# Show the overall score :: all scores are running_total_score = 0 :: int

# Go through each player and get the cards_left_in_your_hand :: int

# Go through each player and get the cards_played_in_this_round :: int

# perform the math :: running_total_score + (cards_played_in_this_round - (2 * cards_left_in_your_hand)) :: int

# Check to see who is the winner.  Sort through each player and evaluate player_name[i] > 75 :: boolean

# If multiple people are > 75 in score, evaluate who has the highest score.

# Print, "player_name[i] is the winner!"

# Create option to (p)lay another round which would save the current game, or (q)uit the program
