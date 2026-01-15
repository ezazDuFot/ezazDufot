"""
Algorithm to pack a luggage bag:

1.⁠ ⁠Separate clothes into heavy, regular, and delicate items.
2.⁠ ⁠Place heavy clothes at the bottom of the bag.
3.⁠ ⁠Place regular clothes in the middle section.
4.⁠ ⁠Wrap delicate clothes and place them on top.
5.⁠ ⁠Keep daily-use accessories easily accessible.
6.⁠ ⁠Ensure space is optimally used.
7.⁠ ⁠Display packing order.
"""

def pack_luggage(heavy, regular, delicate, accessories):
    bag = []

    for item in heavy:
        bag.append(item + " (Bottom)")

    for item in regular:
        bag.append(item + " (Middle)")

    for item in delicate:
        bag.append(item + " (Top - Protected)")

    for item in accessories:
        bag.append(item + " (Side Pocket)")

    return bag


# Example usage
heavy_clothes = ["Jeans", "Jacket"]
regular_clothes = ["T-shirts", "Shirts"]
delicate_clothes = ["Formal Dress"]
accessories = ["Belt", "Socks", "Charger"]

packed_bag = pack_luggage(heavy_clothes, regular_clothes, delicate_clothes, accessories)

print("Luggage Packing Order:")
for item in packed_bag:
    print("-", item)
