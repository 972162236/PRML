import unittest
import numpy as np
import prml.autodiff as autodiff


class TestSigmoid(unittest.TestCase):

    def test_sigmoid(self):
        npx = np.random.randn(3, 5)
        x = autodiff.asarray(npx)
        y = autodiff.sigmoid(x)
        self.assertTrue(np.allclose(y.value, np.tanh(npx * 0.5) * 0.5 + 0.5))

        npg = np.random.randn(3, 5)
        y.backprop(npg)
        self.assertTrue(np.allclose(x.grad, npg * y.value * (1 - y.value)))


if __name__ == "__main__":
    unittest.main()