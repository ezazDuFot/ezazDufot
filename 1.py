"""
Algorithm to arrange clothes in an almirah:

1.⁠ ⁠Take the list of clothes with their categories.
2.⁠ ⁠Group clothes based on category (formal, casual, traditional, etc.).
3.⁠ ⁠Decide priority of categories based on usage frequency.
4.⁠ ⁠Assign top shelves to most-used categories.
5.⁠ ⁠Place less-used categories on lower shelves.
6.⁠ ⁠Ensure no shelf is overloaded.
7.⁠ ⁠Display the final shelf-wise arrangement.
"""

def arrange_almirah(clothes, shelves):
    arrangement = {}
    shelf_number = 1

    for category in clothes:
        if shelf_number > shelves:
            break
        arrangement[f"Shelf {shelf_number}"] = clothes[category]
        shelf_number += 1

    return arrangement


# Example usage
clothes = {
    "Casual Wear": ["T-shirt", "Jeans", "Shirt"],
    "Formal Wear": ["Blazer", "Formal Shirt", "Trousers"],
    "Traditional Wear": ["Kurta", "Sherwani"],
    "Sports Wear": ["Track Pants", "Jersey"]
}

total_shelves = 4

final_arrangement = arrange_almirah(clothes, total_shelves)

for shelf, items in final_arrangement.items():
    print(shelf, "->", items)
