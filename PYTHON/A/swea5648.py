dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = dict()
    emitted, atom_idx = 0, 0
    for n in range(N):
        x, y, d, e = map(int, input().split())
        atoms[atom_idx] = (x * 2, y * 2, d, e)
        atom_idx += 1

    while atoms:  # move
        atom_coordinates = []
        for i in range(atom_idx):
            if atoms.get(i) is None:
                continue
            x, y, d, e = atoms[i]
            nx, ny = x + dr[d], y + dc[d]

            # delete if out of box
            if not (abs(nx) <= 2000 and abs(ny) <= 2000):
                del atoms[i]
            # update atom coordinates
            else:
                if nx < 0:
                    nx = 2000 - nx
                if ny < 0:
                    ny = 2000 - ny
                try:
                    arr[ny][nx].append(i)
                except:
                    print(ny, nx)
                atom_coordinates.append((ny, nx))
        for y, x in atom_coordinates:
            if len(arr[y][x]) > 1:
                for a in arr[y][x]:
                    emitted += atoms[a][-1]
                    del atoms[a]


