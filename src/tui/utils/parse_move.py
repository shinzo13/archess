def parse_move(move_str: str):
    if len(move_str) != 4:
        return None

    try:
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        from_col = col_map[move_str[0].lower()]
        from_row = 8 - int(move_str[1])

        to_col = col_map[move_str[2].lower()]
        to_row = 8 - int(move_str[3])

        return (from_row, from_col), (to_row, to_col)
    except (KeyError, ValueError):
        return None