import unittest
from multiset import MultiSet


class TestMultiSetEqual(unittest.TestCase):

    def test_equal_same_set(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(234)
        x.insert(1)
        y = MultiSet()
        y.insert(3)
        y.insert(2)
        y.insert(234)
        y.insert(1)
        self.assertEqual(x == y, True)

    def test_equal_different_set(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        y = MultiSet()
        y.insert(3)
        y.insert(234)
        y.insert(1)
        self.assertEqual(x == y, False)

    def test_equal_empty_set(self):
        x = MultiSet()
        y = MultiSet()
        self.assertEqual(x == y, True)


class TestRepr(unittest.TestCase):

    def test_repr_with_obj(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(1)
        self.assertEqual(repr(x), 'MultiSet([1, 2, 3])')

    def test_repr_without_obj(self):
        x = MultiSet()
        self.assertEqual(repr(x), 'MultiSet([])')


class TestInsert(unittest.TestCase):

    def test_insert_with_number(self):
        x = TestRepr()
        x.test_repr_with_obj()

    def test_insert_with_bool(self):
        x = MultiSet()
        x.insert(True)
        x.insert(False)
        x.insert(True)
        self.assertEqual(repr(x), 'MultiSet([0, 1, 1])')

    def test_insert_with_numbers(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(42)
        x.insert(1)
        y = MultiSet()
        y.insert(x)
        self.assertEqual(repr(y), 'MultiSet([MultiSet([1, 2, 3, 42])])')


class TestClear(unittest.TestCase):

    def test_clear(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(234)
        x.clear()
        self.assertEqual(repr(x), 'MultiSet([])')


class TestLessEqualTo(unittest.TestCase):

    def test_with_same_set(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(50)
        y = MultiSet()
        y.insert(3)
        y.insert(2)
        y.insert(50)
        self.assertEqual(y <= x, True)

    def test_with_diff_set(self):
        x = MultiSet()
        x.insert(3)
        x.insert(50)
        y = MultiSet()
        y.insert(3)
        y.insert(2)
        y.insert(50)
        self.assertEqual(x <= y, True)

    def test_with_wrong_set(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(50)
        y = MultiSet()
        y.insert(7)
        y.insert(5)
        y.insert(7680)
        self.assertEqual(y <= x, False)


class TestContains(unittest.TestCase):

    def test_contains_number_right(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(234)
        self.assertEqual(2 in x, True)

    def test_contains_number_wrong(self):
        x = MultiSet()
        x.insert(3)
        x.insert(2)
        x.insert(234)
        self.assertEqual(5 in x, False)

    def test_contains_bool_right(self):
        x = MultiSet()
        x.insert(True)
        x.insert(False)
        x.insert(234)
        self.assertEqual(1 in x, True)

    def test_contains_bool_wrong(self):
        x = MultiSet()
        x.insert(True)
        x.insert(True)
        x.insert(234)
        self.assertEqual(0 in x, False)


class TestLen(unittest.TestCase):

    def test_len_with_set(self):
        x = MultiSet()
        x.insert(True)
        x.insert(True)
        x.insert(234)
        self.assertEqual(len(x), 3)

        def test_len_without_set(self):
            x = MultiSet()
            self.assertEqual(len(x), 0)


class TestRemove(unittest.TestCase):

    def test_remove_with_valid_num(self):
        x = MultiSet()
        x.insert(True)
        x.insert(True)
        x.insert(234)
        self.assertEqual(x.remove(1), 1)

    def test_remove_without_valid_num(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        self.assertEqual(x.remove(22), None)

    def test_remove_without_middle_num(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        self.assertEqual(x.remove(2), 2)

    def test_remove_without_end_num(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        self.assertEqual(x.remove(3), 3)


class TestCount(unittest.TestCase):

    def test_count_with_one(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        self.assertEqual(x.count(2), 1)

    def test_count_with_multiple(self):
        x = MultiSet()
        x.insert(1)
        x.insert(1)
        x.insert(3)
        self.assertEqual(x.count(1), 2)

    def test_count_with_multiple(self):
        x = MultiSet()
        x.insert(1)
        x.insert(1)
        x.insert(3)
        self.assertEqual(x.count(23), 0)


class TestSub(unittest.TestCase):

    def test_correct_sub(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(5)
        z = y - x
        self.assertEqual(repr(z), 'MultiSet([5])')

    def test_correct_sub_2(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(5)
        z = x - y
        self.assertEqual(repr(z), 'MultiSet([3])')

    def test_not_correct_sub(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(3)
        z = x - y
        self.assertEqual(repr(z), 'MultiSet([])')


class TestiSub(unittest.TestCase):

    def test_correct_isub(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(5)
        y -= x
        self.assertEqual(repr(y), 'MultiSet([5])')

    def test_correct_isub_2(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(5)
        x -= y
        self.assertEqual(repr(x), 'MultiSet([3])')

    def test_not_correct_isub(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(3)
        x -= y
        self.assertEqual(repr(x), 'MultiSet([])')


class Testiadd(unittest.TestCase):

    def test_correct_iadd(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        y.insert(5)
        y += x
        self.assertEqual(repr(y), 'MultiSet([1, 2, 3, 4, 5])')

    def test_correct_iadd_2(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        y.insert(5)
        y.insert(6)
        x += y
        self.assertEqual(repr(x), 'MultiSet([1, 2, 3, 4, 5, 6])')

    def test_empty_correct_iadd(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        x += y
        self.assertEqual(repr(x), 'MultiSet([1, 2, 3])')


class Testand(unittest.TestCase):

    def test_correct_and(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(5)
        z = y & x
        self.assertEqual(repr(z), 'MultiSet([1, 2])')

    def test_correct_and_2(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        y.insert(5)
        y.insert(6)
        z = x & y
        self.assertEqual(repr(z), 'MultiSet([])')

    def test_empty_correct_and(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        z = x & y
        self.assertEqual(repr(z), 'MultiSet([])')


class TestIsDisJoint(unittest.TestCase):

    def test_same_elements(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(1)
        y.insert(2)
        y.insert(3)
        self.assertEqual(x.isdisjoint(y), False)

    def test_diff_elements_1(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        y.insert(5)
        y.insert(6)
        self.assertEqual(x.isdisjoint(y), True)

    def test_diff_elements_2(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        self.assertEqual(x.isdisjoint(y), True)

    def test_empty_set_1(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        self.assertEqual(x.isdisjoint(y), True)

    def test_empty_set_2(self):
        x = MultiSet()
        y = MultiSet()
        self.assertEqual(x.isdisjoint(y), False)


class TestAdd(unittest.TestCase):

    def test_correct_add(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        y.insert(5)
        z = y + x
        self.assertEqual(repr(z), 'MultiSet([1, 2, 3, 4, 5])')

    def test_correct_add_2(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        y.insert(5)
        y.insert(6)
        z = x + y
        self.assertEqual(repr(z), 'MultiSet([1, 2, 3, 4, 5, 6])')

    def test_empty_correct_add(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        z = x + y
        self.assertEqual(repr(z), 'MultiSet([1, 2, 3, None])')


class TestiAnd(unittest.TestCase):

    def test_correct_iand(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(4)
        y.insert(5)
        x &= y
        self.assertEqual(repr(x), 'MultiSet([])')

    def test_correct_iand_2(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(3)
        y.insert(2)
        y.insert(6)
        x &= y
        self.assertEqual(repr(x), 'MultiSet([2, 3])')

    def test_empty_correct_iand(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        x &= y
        self.assertEqual(repr(x), 'MultiSet([])')

    def test_unbalanced_correct_iand(self):
        x = MultiSet()
        x.insert(1)
        x.insert(2)
        x.insert(3)
        y = MultiSet()
        y.insert(2)
        x.insert(55)
        x &= y
        self.assertEqual(repr(x), 'MultiSet([2])')

unittest.main(exit=False)
