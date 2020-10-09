# Peak finder 1D array O(n)

class Peak:

  def __init__(self, array):
    self.array = array

  def find(self):
    peaks = []
    for i in range(len(self.array)):
      if i == 0:
        peak = self.array[i]
        if peak > self.array[i+1]:
          peaks.append(i)
      elif i == (len(self.array)-1):
        peak = self.array[i]
        if peak > self.array[i-1]:
          peaks.append(i)
      else:
        peak = self.array[i]
        if (peak > self.array[i-1]) and (peak > self.array[i+1]):
          peaks.append(i)
    return peaks
