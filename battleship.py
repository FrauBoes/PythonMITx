#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:34:23 2017

@author: thelma
"""
from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print(' '.join(row))

def random_row(board_in):
  return randint(0, len(board_in))

def random_col(board_in):
  return randint(0, len(board_in))

print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess Row: "))
guess_col = int(input('Guess Col: '))

if guess_row == ship_row and guess_col == ship_col:
    print('Congratulations! You sank my battleship!')
else: 
    if guess_row not in range(len(board)) or \
       guess_col not in range(len(board)):
        print("Oops, that's not even in the ocean")
    else:
        print('You missed my battleship!')
        board[guess_row-1][guess_col-1] = 'X'
        print_board(board)