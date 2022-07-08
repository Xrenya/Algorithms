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
    >>> InsertationSort([5, 4, 3, 2, 1])
    [0, 1, 2, 3, 4, 5]
    >>> InsertationSort([5, 4, 3, 2, 1], ascending=False)
    [5, 4, 3, 2, 1, 0]
    >>> InsertationSort([]) == sorted([])
    True
    >>> InsertationSort([5, -423, 3, -10]) == sorted([-423, -10, 3, 5])
    True
    >>> InsertationSort(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> InsertationSort(array) == sorted(array)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> InsertationSort(array) == sorted(array)
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


def insertation_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            j -= 1
    return array
