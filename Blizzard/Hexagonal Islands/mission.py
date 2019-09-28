from typing import Set, Iterable

class HexField:
    def __init__(self, coast, index_1='ABCDEFGHIJKL', index_2='123456789'):
        self.idx1, self.idx2 = index_1, index_2
        self.coast = set(coast)
        self.sea = set()
        self.land = set(coast)
        self.islands = []
        self._fill_field()
        print('map processed\n', self)

    def __str__(self):
        s = f'HexField\n\tCoast {len(self.coast):>5}  => ' +\
            f'{" ".join(sorted(self.coast))}' +\
            f'\n\tLands {len(self.land):>5}  => ' +\
            f'{" ".join(sorted(self.land))}' + \
            f'\n\tInner {len(self.land-self.coast):>5}' +\
            f'  => {" ".join(sorted(self.land-self.coast))}' +\
            f'\n\tSea   {len(self.sea):>5}' + \
            f'\n\tTotal {len(self.idx1)*len(self.idx2):>5}\n'
        if self.islands:
            s += f'\tIslands {len(self.islands):>3}\n'
            for i, isl in enumerate(self.islands):
                s += f'\t\t#{i+1:>2} S={len(isl)} ' +\
                     f'=> {" ".join(sorted(isl))}\n'
        return s

    def _get_neighb(self, cell: str):
        neig, c0, c1 = [], cell[0], cell[1]
        i1, i2 = self.idx1.index(c0), self.idx2.index(c1)
        if i1:  # not first row
            # left direct
            neig.append(self.idx1[i1 - 1] + c1)
            # left indirect
            if i1 % 2 and c1 != self.idx2[-1]:  # 'BDFHJL'
                neig.append(self.idx1[i1 - 1] + self.idx2[i2 + 1])
            if not i1 % 2 and i2:  # ACEGIK
                neig.append(self.idx1[i1 - 1] + self.idx2[i2 - 1])
        if i2:                              # not first line -> up
            neig.append(c0 + self.idx2[i2 - 1])
        if c1 != self.idx2[-1]:             # not last line -> down
            neig.append(c0 + self.idx2[i2 + 1])
        if c0 != self.idx1[-1]:  # not last row
            # right direct
            neig.append(self.idx1[i1 + 1] + c1)
            # right indirect
            if i1 % 2 and c1 != self.idx2[-1]:  # 'BDFHJL'
                neig.append(self.idx1[i1 + 1] + self.idx2[i2 + 1])
            if not i1 % 2 and i2:  # ACEGIK
                neig.append(self.idx1[i1 + 1] + self.idx2[i2 - 1])
        return neig

    def _fill_field(self):
        # first pass - mark sea and inner land
        processed = set()
        for cell in (i + j for i in self.idx1 for j in self.idx2):
            if cell not in processed:
                processed.add(cell)
                if not(cell in self.coast or cell in self.land or \
                        self._is_inner_land(cell)):
                    self._mark_sea(cell, processed)
        # second pass - from lands make islands
        processed = set(self.sea)
        for cell in self.land:
            if cell not in processed:
                processed.add(cell)
                island = [cell]
                to_do = [cell]
                while to_do:
                    for neig in self._get_neighb(to_do.pop()):
                        if neig in self.land and neig not in processed:
                            # found next cell of this island
                            island.append(neig)
                            to_do.append(neig)
                            processed.add(neig)
                self.islands.append(sorted(island))
        self.islands.sort(key=len)

    def _is_map_border(self, cell):
        if 0 < (i1 := self.idx1.index(cell[0])) < len(self.idx1)-1 \
            and 0 < (i2 := self.idx2.index(cell[1])) < len(self.idx2)-1:
            return False
        else:
            return True

    def _is_inner_land(self, cell):
        # test, is cell have access to borders, or all around it - is cost
        if self._is_map_border(cell):
            return False
        to_do = [cell]
        tested = {cell}
        while to_do:
            for neig in self._get_neighb(to_do.pop()):
                if neig not in self.coast and neig not in tested:
                    if self._is_map_border(neig):
                        # tested is sea cell, it have access to field borders
                        return False
                    tested.add(neig)
                    to_do.append(neig)
        # can't reach borders, it inside coast cells
        self.land.update(tested)
        return True

    def _mark_sea(self, cell, processed):
        to_do = [cell]
        self.sea.add(cell)
        while to_do:
            for neig in self._get_neighb(to_do.pop()):
                if neig not in self.coast and neig not in processed:
                    self.sea.add(neig)
                    to_do.append(neig)
                    processed.add(neig)


def hexagonal_islands(coasts: Set[str]) -> Iterable[int]:
    field = HexField(coasts)
    islands_sizes = sorted([len(isl) for isl in field.islands])
    return islands_sizes



if __name__ == '__main__':
    assert(sorted(hexagonal_islands({'C5', 'E5', 'F4', 'F5', 'H4', 'H5', 'I4', 'I6', 'J4', 'J5'}))) == [1, 3, 7]
    assert(sorted(hexagonal_islands({'A1', 'A2', 'A3', 'A4', 'B1', 'B4', 'C2', 'C5', 'D2', 'D3', 'D4', 'D5',
                                     'H6', 'H7', 'H8', 'I6', 'I9', 'J5', 'J9', 'K6', 'K9', 'L6', 'L7', 'L8'}))) == [16, 19]
    print('The local tests are done. Click on "Check" for more real tests.')
