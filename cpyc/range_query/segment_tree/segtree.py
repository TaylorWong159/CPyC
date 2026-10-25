from typing import Callable

class SegmentTree[T]:
    def __init__(self, arr: list[T], op: Callable[[T, T], T], null: T) -> None:
        self.op = op
        self.null = null
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.arr = [null for _ in range(self.n)]
        self._build(0, 0, self.n, arr)

    def L(self, i: int) -> int:
        return (i << 1) + 1

    def R(self, i: int) -> int:
        return (i << 1) + 2

    def M(self, l: int, r: int) -> int:
        return (l + r) // 2

    def _build(self, i: int, l: int, r: int, arr: list[T]) -> T:
        if r - l == 1:
            self.arr[i] = arr[l] if l < len(arr) else self.null
            return self.arr[i]
        self.arr[i] = self.op(
            self._build(self.L(i), l, self.M(l, r), arr),
            self._build(self.R(i), self.M(l, r), r, arr)
        )
        return self.arr[i]

    def query(self, l: int, r: int) -> T:
        return self._query(0, 0, self.n, l, r)

    def _query(self, i: int, sl: int, sr: int, tl: int, tr: int) -> T:
        if sr <= tl or sl >= tr:
            return self.null
        if tl <= sl < sr <= tr:
            return self.arr[i]
        return self.op(
            self._query(self.L(i), sl, self.M(sl, sr), tl, tr),
            self._query(self.R(i), self.M(sl, sr), sr, tl, tr)
        )

    def update(self, i: int, op: Callable[[T], T]) -> None:
        self._update(0, 0, self.n, i, op)

    def _update(self, i: int, l: int, r: int, t: int, op: Callable[[T], T]) -> T:
        if l == r:
            self.arr[i] = op(self.arr[i])
            return self.arr[i]
        if t < self.M(l, r):
            self._update(self.L(i), l, self.M(l, r), t, op)
        else:
            self._update(self.R(i), self.M(l, r), r, t, op)
        self.arr[i] = self.op(self.arr[self.L(i)], self.arr[self.R(i)])
        return self.arr[i]