#!/usr/bin/env python
"""Utility classes for a deck of cards."""


from enum import Enum


Suit = Enum("Suit", "Spades Clubs Hearts Diamonds")


Value = Enum(
    "Value", "Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King Joker"
)


class Card:
    """Basic card class."""

    def __init__(self, new_suit, new_value):
        self.suit = new_suit
        self.value = new_value

    def __repr__(self):
        """Outputs the object."""

        return f"{self.value.name} of {self.suit.name}"


class Deck:
    """Deck class."""

    def __init__(self):
        self.generate_cards()

    def generate_cards(self):
        """Generates all the cards in a deck."""

        cards = []
        for suit in Suit:
            for value in Value:
                cards.append(Card(suit, value))

        self.cards = cards
