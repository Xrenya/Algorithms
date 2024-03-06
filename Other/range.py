def rrange(start, end, step=1):
    if start <= end:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start -= step
