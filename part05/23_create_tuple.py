def create_tuple(x: int, y: int, z: int):
    my_list = [x, y, z]
    my_list.sort()

    return (my_list[0], my_list[-1], sum(my_list))