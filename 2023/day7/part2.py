# start 2:08 pm Dec 9, 2023
# end 2:49 (used and instead of or)
# Operator symbols (e.g +, -) as functions. Also, some other neat function
import operator
import functools

@functools.total_ordering
class Hand:
    def __init__(self, hand_value):
        self.hand_value = hand_value
    
    def __eq__(self, other):
        return self.hand_value == other.hand_value
    def __lt__(self, other):
        for card_number in range(len(self.hand_value)):
            if (self.camel_card_character_ranking(self.hand_value[card_number]) <
                other.camel_card_character_ranking(other.hand_value[card_number])):
                return True
            elif (self.camel_card_character_ranking(self.hand_value[card_number]) >
                other.camel_card_character_ranking(other.hand_value[card_number])):
                return False

    def camel_card_character_ranking(self, card_char):
        character = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        point_values = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        character_point_values = {card_character : card_value for card_character, card_value in zip(character, point_values)}
        return character_point_values[card_char]

def day7():
    joker = "J"
    # all_hands is dictionary of hand to point value
    all_hands = []
    with open("input.txt", "r") as file:
        for line in file:
            all_hands.append(line.split())
    
    all_hand_by_type = [[] for x in range(7)]
    # Loops through key, and categorize hand by type of hand
    for hand_value_pair in all_hands:
        hand = hand_value_pair[0]
        # gets card count ratio. I don't need to know if there are 5 Aces, just that there is
        # 5 of 1 card.
        character_counts = { character : operator.countOf(hand, character) for character in set(hand)}
        char_freq_wo_joker = { character : operator.countOf(hand, character) for character in set(hand)}
        try:
            del char_freq_wo_joker[joker]
        except:
            pass
        # Descending result using frequency value which has index of 1
        # Only 1 character = 1 card = 5 of a kind
        if ((len(character_counts) == 1) or 
            (len(character_counts) == 2 and joker in character_counts)):
            all_hand_by_type[0].append(hand_value_pair)
        # Four of a kind. 
        elif ((len(character_counts) == 2 and character_counts[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 4) or
              (len(character_counts) == 3 and joker in character_counts and 
               character_counts[joker] + char_freq_wo_joker[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 4)):
            all_hand_by_type[1].append(hand_value_pair)
        # Full House
        elif ((len(character_counts) == 2 and character_counts[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 3) or 
              (len(character_counts) == 3 and joker in character_counts and 
               character_counts[joker] + char_freq_wo_joker[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 3)):
            all_hand_by_type[2].append(hand_value_pair)
        # 3 of a kind
        elif ((len(character_counts) == 3 and character_counts[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 3) or 
              (len(character_counts) == 4 and joker in character_counts and 
               character_counts[joker] + char_freq_wo_joker[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 3)):
            all_hand_by_type[3].append(hand_value_pair)
        # 2 Pair
        elif ((len(character_counts) == 3 and character_counts[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 2) or 
              (len(character_counts) == 4 and joker in character_counts and 
               character_counts[joker] + char_freq_wo_joker[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 2)):
            all_hand_by_type[4].append(hand_value_pair)
        # 1 Pair
        elif ((len(character_counts) == 4 and character_counts[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 2) or 
              (len(character_counts) == 5 and joker in character_counts and 
               character_counts[joker] + char_freq_wo_joker[max(char_freq_wo_joker, key=char_freq_wo_joker.get)] == 2)):
            all_hand_by_type[5].append(hand_value_pair)
        # Highest Card
        else:
            all_hand_by_type[6].append(hand_value_pair)
    
    # Sort for ranking withing hand types
    for hand_type_collection in all_hand_by_type:
        hand_type_collection.sort(reverse=True, key=lambda hand : Hand(hand[0]))
    
    # Calculate point total
    point_total = 0
    starting_single_hand_point = len(all_hands)

    print(all_hand_by_type[6])
    print("---------------")

    for hand_type_number in range(len(all_hand_by_type)):
        for hand_value_pair_number in range(len(all_hand_by_type[hand_type_number])):
            bid_value = int(all_hand_by_type[hand_type_number][hand_value_pair_number][1])
#            print(all_hand_by_type[hand_type_number][hand_value_pair_number])
            point_total = point_total + (bid_value * starting_single_hand_point)
            starting_single_hand_point -= 1
    print(point_total)
    
day7()
