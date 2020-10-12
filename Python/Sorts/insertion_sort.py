"""
A pure Python implementation of the insertion sort algorithm.
"""

def InsertationSort(array: list, ascending=True) -> list:
  """A Python implementation of the insertion sort algorithm
    :param array: some mutable ordered collection with heterogeneous
    comparable items inside
    :param ascending: boolean value whether is ascending or descending order.
    :return: the same collection ordered by ascending
    Examples:
    >>> InsertationSort([5, 4, 3, 2, 1]).sort()
    [0, 1, 2, 3, 4, 5]
    >>> insertion_sort([]) == sorted([])
    True
    >>> InsertationSort([5, -423, 3, -10]).sort() == sorted([-423, -10, 3, 5])
    True
    >>> insertion_sort(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> InsertationSort(array).sort() == sorted(array)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> InsertationSort(array).sort() == sorted(array)
    True
    """
  if ascending:
    for j in range(1, len(array)):
      key = array[j]
      i = j - 1
      while (i>-1) and (array[i]>key):
        array[i+1] = array[i]
        i -= 1
      array[i+1] = key
  else:
    for j in range(1, len(array)):
      key = array[j]
      i = j - 1
      while (i>-1) and (array[i]<key):
        array[i+1] = array[i]
        i -= 1
      array[i+1] = key
  return array
