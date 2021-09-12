#
# メソッドチェーン可能なiterator
#

from __future__ import annotations

from typing import Any, Callable, Iterable, List


class ChainableIterator():

    """
    メソッドチェーン可能なイテレータを生成するクラス。
    """

    def __init__(self, iter: Iterable) -> None:
        """
        iterableなオブジェクトからChainableIteratorを生成します。

        Args:
            iter (Iterable) : ChainableIteratorが反復処理を行うためのiterableオブジェクト。
        """
        self.iter = iter

    def map(self, func: Callable[[Any], Any]) -> ChainableIterator:
        self.iter = map(func, self.iter)
        return self
    
    def filter(self, func: Callable[[Any], Any]) -> ChainableIterator:
        self.iter = filter(func, self.iter)
        return self

    def as_list(self) -> List[Any]:
        return list(self.iter)
