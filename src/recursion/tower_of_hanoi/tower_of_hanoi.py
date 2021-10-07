from util.counter import Counter
from src.recursion.tower_of_hanoi.input import towers

@Counter
def move_plates(plates: list, from_tower: str, to_tower: str):
    if len(plates) == 1:
        plate = plates[0]
        print(f'Moving plate {plate} from {from_tower} to {to_tower}')
    else:
        tower_set_moving = set([from_tower, to_tower])
        third_tower = list(tower_set - tower_set_moving)[0]
        previous_plates = plates[:-1]
        last_plate = plates[-1:]
        move_plates(previous_plates, from_tower, third_tower)
        move_plates(last_plate, from_tower, to_tower)
        move_plates(previous_plates, third_tower, to_tower)


if __name__ == '__main__':
    tower_set = set(towers)
    move_plates(towers['A'], 'A', 'C')
    print(f'The task is done in {move_plates.counter} operations.')
