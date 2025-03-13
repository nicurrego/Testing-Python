import unittest

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertNotEqual('hola', 'cami')

    def test_assert_true_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int('x2')

    def test_assert_in(self):
        self.assertIn(10, [2,3,4,5,10])
        self.assertNotIn(10, [1,2,3,4,5,6])

    def test_assert_dicts(self):
        user = {"First_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"First_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1,2,3},
            {1,2,3}
        )