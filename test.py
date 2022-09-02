for a in [True, False]:
    for b in [True, False]:
        print(f'\n({a}, {b}): {not a or not b}')
        print(f'({a}, {b}): {not (a and b)}')