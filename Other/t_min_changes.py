# Given start word "cat" and end word "dog"
# and word list: ["can", "dan", "don", "dog", "dag"]
# everytime you can change only one letter at time
# find the smallest number of changes to reach target word from starting word
# "cat" -> "dan" -> "don" -> "dog": 3 changes
# make a graph for each word and use dfs  with visted words to reach the target word with counter
