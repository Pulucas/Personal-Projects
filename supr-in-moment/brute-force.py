chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "-"]

def generate_combinations(chars, length, prefix=""):
    if length == 0:
        # note: takes way less time to run without printing
        print(prefix)
        return
    for char in chars:
        generate_combinations(chars, length - 1, prefix + char)

# takes exponentially longer to run as i (length of the array of letters) increases
for i in range(1, 9):
  print(i)
  generate_combinations(chars, i)