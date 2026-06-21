def top_n(items, n):
    """
    Returns the top n items from a list based on their values.

    Parameters:
    items (list): A list of tuples where each tuple contains an item and its value.
    n (int): The number of top items to return.

    Returns:
    list: A list of the top n items sorted by their values in descending order.
    """
    if n <= 0:
        return []

    # Use bubble sort to order items by value in descending order.
    sorted_items = list(items)
    length = len(sorted_items)

    for i in range(length):
        swapped = False
        for j in range(0, length - 1 - i):
            if sorted_items[j][1] < sorted_items[j + 1][1]:
                sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]
                swapped = True
        if not swapped:
            break

    return sorted_items[:n]
