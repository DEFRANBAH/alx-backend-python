#!/usr/bin/python3

def solution(cards, moves, query):
    card_position = {card[0]: [card[2]] for card in cards}

    for move in moves:
        card_id, row_before, col_before, row_after, col_after = move

        if card_id  in card_position:
            card_position[card_id] = [row_after, col_after]
    return card_position[query]
            
