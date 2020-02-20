#!/usr/bin/python

import sys

# def recurse(n, idx):
#   new_combos = []

#   if idx == n - 1:
#     arr = ["rock"] * n
#     for text in ["rock", "paper", "scissors"]:
#       new_combos.append(arr[:-1] + [text])

#   else:
#     print(idx)
#     last_combos = recurse(n, idx + 1)

#     for combo in last_combos:
#       for text in ["rock", "paper", "scissors"]:
#         new_combos.append(combo[:idx] + [text] + combo[idx + 1:])

#   return new_combos

def recurse(n, idx):
  new_combos = []

  if idx == n - 1:
    arr = ["rock"] * n
    for text in ["rock", "paper", "scissors"]:
      new_combos.append(arr[:-1] + [text])
  else:
    last_combos = recurse(n, idx + 1)
    for text in ["rock", "paper", "scissors"]:
      for combo in last_combos:
        new_combos.append(combo[:idx] + [text] + combo[idx + 1:])

  return new_combos

def rock_paper_scissors(n, idx = 0):
  if(n == 0):
    return [[]]

  new_combos = []

  if idx == n - 1:
    arr = ["rock"] * n
    for text in ["rock", "paper", "scissors"]:
      new_combos.append(arr[:-1] + [text])
  else:
    last_combos = rock_paper_scissors(n, idx + 1)
    for text in ["rock", "paper", "scissors"]:
      for combo in last_combos:
        new_combos.append(combo[:idx] + [text] + combo[idx + 1:])

  return new_combos
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')