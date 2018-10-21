#!/usr/bin/env python
"""Utility classes for a deck of cards."""


from enum import Enum


Suit = Enum("Spades", "Clubs", "Hearts", "Diamonds")


Value = Enum(
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Joker",
)


class Card:
    """Basic card class."""

    def __init__(self, new_suit, new_value):
        self.suit = new_suit
        self.value = new_value

    def __repr__(self):
        """Outputs the object."""

        print(f"{self.value} of {self.suit}")
