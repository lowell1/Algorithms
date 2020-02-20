#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  sum = 0

  for i in range(2, n):
    sum += n - i + 1
    print(i,sum)
    # print(f"i = {i}")
    # for j in range(0, n - i + 1):
    #   print(f"j = {j}")

  print(sum)

  """ if(n <= 1):
    return 1

  return n - 1 + eating_cookies(n - 1)"""

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')