dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = dict()
    emitted, atom_idx = 0, 0
    for n in range(N):
        x, y, d, e = map(int, input().split())
        # if x < 0:
        #     x = 1000 - x
        # if y < 0:
        #     y = 1000 - y
        atoms[atom_idx] = (y * 2, x * 2, d, e)
        atom_idx += 1
    # print(atoms)
    while atoms:  # move
        atom_coordinates = dict()
        for i in range(atom_idx):
            if atoms.get(i) is None:
                continue
            y, x, d, e = atoms[i]
            ny, nx = y + dy[d], x + dx[d]

            # delete if out of box
            if not (abs(nx) <= 2000 and abs(ny) <= 2000):
                del atoms[i]
            # update atom coordinates
            else:
                if atom_coordinates.get((ny, nx)) is None:
                    atom_coordinates[(ny, nx)] = [i]
                else:
                    atom_coordinates[(ny, nx)].append(i)
                atoms[i] = (ny, nx, atoms[i][-2], atoms[i][-1])

        for collided in atom_coordinates.values():
            if len(collided) > 1:
                for c in collided:
                    emitted += atoms[c][-1]
                    del atoms[c]
    print(f"#{tc} {emitted}")
