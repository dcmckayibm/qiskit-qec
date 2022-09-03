import unittest

from qiskit_qec.codes.rotated_surface_code import RSSC


class TestRSSC(unittest.TestCase):
    def test_even_distance(self):
        with self.assertRaises(Exception):
            RSSC(4)

    def test_d3(self):
        c = RSSC(3)
        self.assertEqual(c.n, 11)
        self.assertEqual(c.k, 1)
        self.assertEqual(c.d, 3)
        self.assertEqual(c.logical_x, [[0, 3, 6]])
        self.assertEqual(c.logical_z, [[0, 1, 2]])
        self.assertEqual(c.x_boundary, [[0], [3], [6], [2], [5], [8]])
        self.assertEqual(c.z_boundary, [[0], [1], [2], [6], [7], [8]])
        self.assertEqual(
            c.x_gauges,
            [[0, -1, 1], [1, 2, 9], [3, 4, 10], [4, 9, 5], [6, 10, 7], [7, 8, -1]],
        )
        self.assertEqual(
            c.z_gauges,
            [[0, 3, -1], [1, 9, 4], [2, 5, 9], [3, 10, 6], [4, 7, 10], [5, -1, 8]],
        )
        self.assertEqual(
            c.x_stabilizers,
            [[0, -1, 1, 3, 4, 10], [1, 2, 9], [4, 9, 5, 7, 8, -1], [6, 10, 7]],
        )
        self.assertEqual(
            c.z_stabilizers,
            [[0, 3, -1, 1, 9, 4], [2, 5, 9], [3, 10, 6], [4, 7, 10, 5, -1, 8]],
        )

    def test_d5(self):
        c = RSSC(5)
        self.assertEqual(c.n, 33)
        self.assertEqual(c.k, 1)
        self.assertEqual(c.d, 5)
        self.assertEqual(c.logical_x, [[0, 5, 10, 15, 20]])
        self.assertEqual(c.logical_z, [[0, 1, 2, 3, 4]])
        self.assertEqual(c.x_boundary, [[0], [5], [10], [15], [20], [4], [9], [14], [19], [24]])
        self.assertEqual(c.z_boundary, [[0], [1], [2], [3], [4], [20], [21], [22], [23], [24]])
        self.assertEqual(
            c.x_gauges,
            [
                [0, -1, 1],
                [1, 2, 25],
                [2, -1, 3],
                [3, 4, 26],
                [5, 6, 27],
                [6, 25, 7],
                [7, 8, 28],
                [8, 26, 9],
                [10, 27, 11],
                [11, 12, 29],
                [12, 28, 13],
                [13, 14, 30],
                [15, 16, 31],
                [16, 29, 17],
                [17, 18, 32],
                [18, 30, 19],
                [20, 31, 21],
                [21, 22, -1],
                [22, 32, 23],
                [23, 24, -1],
            ],
        )
        self.assertEqual(
            c.z_gauges,
            [
                [0, 5, -1],
                [1, 25, 6],
                [2, 7, 25],
                [3, 26, 8],
                [4, 9, 26],
                [5, 27, 10],
                [6, 11, 27],
                [7, 28, 12],
                [8, 13, 28],
                [9, -1, 14],
                [10, 15, -1],
                [11, 29, 16],
                [12, 17, 29],
                [13, 30, 18],
                [14, 19, 30],
                [15, 31, 20],
                [16, 21, 31],
                [17, 32, 22],
                [18, 23, 32],
                [19, -1, 24],
            ],
        )
        self.assertEqual(
            c.x_stabilizers,
            [
                [0, -1, 1, 5, 6, 27],
                [1, 2, 25],
                [2, -1, 3, 7, 8, 28],
                [3, 4, 26],
                [6, 25, 7, 11, 12, 29],
                [8, 26, 9, 13, 14, 30],
                [10, 27, 11, 15, 16, 31],
                [12, 28, 13, 17, 18, 32],
                [16, 29, 17, 21, 22, -1],
                [18, 30, 19, 23, 24, -1],
                [20, 31, 21],
                [22, 32, 23],
            ],
        )
        self.assertEqual(
            c.z_stabilizers,
            [
                [0, 5, -1, 1, 25, 6],
                [2, 7, 25, 3, 26, 8],
                [4, 9, 26],
                [5, 27, 10],
                [6, 11, 27, 7, 28, 12],
                [8, 13, 28, 9, -1, 14],
                [10, 15, -1, 11, 29, 16],
                [12, 17, 29, 13, 30, 18],
                [14, 19, 30],
                [15, 31, 20],
                [16, 21, 31, 17, 32, 22],
                [18, 23, 32, 19, -1, 24],
            ],
        )


if __name__ == "__main__":
    unittest.main()
