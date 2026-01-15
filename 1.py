"""Algorithm: Packing Clothes in a Luggage Bag

1. Start
2. Identify trip duration and activities
3. List required clothes and accessories
4. Separate clothes into categories
5. Roll casual clothes to save space
6. Fold formal and delicate clothes
7. Place heavy items at the bottom
8. Keep frequently used items on top
9. End
"""

# Code Implementation

def pack_luggage():
    luggage = {
        "Bottom Layer": ["Shoes", "Jeans"],
        "Middle Layer": ["T-shirts", "Casual Wear"],
        "Top Layer": ["Formal Dress", "Delicate Clothes"],
        "Side Pouch": ["Socks", "Accessories"]
    }

    return luggage


# Example usage
packed_items = pack_luggage()

for section, items in packed_items.items():
    print(section, ":", items)
