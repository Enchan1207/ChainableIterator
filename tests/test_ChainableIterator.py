#
# ChainableIteratorのテスト
#

import unittest
import random

from src.chainableiterator.chainableiterator import ChainableIterator
from termdecorator import termdecorate


class testChainableIterator(unittest.TestCase):

    def setUp(self) -> None:
        # 元データを生成しておく
        self.datas = range(random.randint(1, 1000))
        self.ci = ChainableIterator(self.datas)

    @termdecorate
    def testConvertToList(self):
        """ list変換 """
        self.assertEqual(list(self.datas), self.ci.as_list())
    
    @termdecorate
    def testApplyMap(self):
        """ map関数の適用 """
        
        # map
        fc_square = lambda n: n * 2
        ci_ = self.ci.map(fc_square)
        datas_applied = map(fc_square, self.datas)

        self.assertEqual(list(datas_applied), ci_.as_list())

    @termdecorate
    def testApplyFilter(self):
        """ filter関数の適用 """

        # filter
        filter_even = lambda n: n % 2 == 0
        ci_ = self.ci.filter(filter_even)
        datas_applied = filter(filter_even, self.datas)

        self.assertEqual(list(datas_applied), ci_.as_list())

    @termdecorate
    def testApplyMultipleFunctions(self):
        """ 複数の関数を同時に適用する """
        ci_ = self.ci

        fc_square = lambda n: n * 2
        filter_even = lambda n: n % 2 == 0
        ci_.filter(filter_even) \
            .map(fc_square)

        datas_applied = filter(filter_even, self.datas)
        datas_applied = map(fc_square, datas_applied)

        self.assertEqual(list(datas_applied), ci_.as_list())
            
if __name__ == '__main__':
    unittest.main()
