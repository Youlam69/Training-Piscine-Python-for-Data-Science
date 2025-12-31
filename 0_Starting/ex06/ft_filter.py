def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is not None:
        for item in iterable:
            if function(item):
                yield item
    else:
        for item in iterable:
            if item:
                yield item
