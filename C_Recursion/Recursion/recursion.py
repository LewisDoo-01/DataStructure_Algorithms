# 1 - Return True if target is found in indicated portion of a Python list.
def binary_search(data, target, low, high):
  if low > high:
    return False                    # interval is empty; no match
  else:
    mid = (low + high) // 2
    if target == data[mid]:         # found a match
      return True
    elif target < data[mid]:
      # recur on the portion left of the middle
      return binary_search(data, target, low, mid - 1)
    else:
      # recur on the portion right of the middle
      return binary_search(data, target, mid + 1, high)

# 2 - Return the sum of the numbers in implicit slice S[start:stop].
def binary_sum(S, start, stop):
  if start >= stop:                      # zero elements in slice
    return 0
  elif start == stop-1:                  # one element in slice
    return S[start]
  else:                                  # two or more elements in slice
    mid = (start + stop) // 2
    return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

# 3- Return n!
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# 4- Return the nth Fibonacci number
def fibonacci(n):
  if n <= 1:
      return n
  else:
      return(fibonacci(n-1) + fibonacci(n-2))

# 5- Return the sum of the first n numbers of sequence S
def linear_sum(S, n):
  if n == 0:
    return 0
  else:
    return linear_sum(S, n-1) + S[n-1]

# 6- Compute the value x^n for integer n
def power(x, n):
  if n == 0:
    return 1
  else:
    return x * power(x, n-1)

# 7- Reverse elements in implicit slice S[start:stop]
def reverse(S, start, stop):
  if start < stop - 1:                         # if at least 2 elements:
    S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
    reverse(S, start+1, stop-1)                # recur on rest

# 8- Return True if there are no duplicate elements in slice S[start:stop].
def unique(S, start, stop):
  if stop - start <= 1: return True                # at most one item
  elif not unique(S, start, stop-1): return False  # first part has duplicate
  elif not unique(S, start+1, stop): return False  # second part has duplicate
  else: return S[start] != S[stop-1]               # do first and last differ?

def tail_recursion(n):
  if n > 0:
    print(n, end = ' ')
    tail_recursion(n-1)