# Move a tower of height-1 to an intermediate pole, using the final pole.
# Move the remaining disk to the final pole.
# Move the tower of height-1 from the intermediate pole to the final pole using the original pole.


def move_tower(height, from_pole, to_pole, middle_pole):
    if height >= 1:
        move_tower(height-1, from_pole, middle_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, middle_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):
    print(f"moving disk from {from_pole} to {to_pole}")


if __name__ == '__main__':

    move_tower(4, "A", "C", "B")