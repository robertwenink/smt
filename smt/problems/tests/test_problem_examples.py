import unittest

import matplotlib
import matplotlib.pyplot

matplotlib.use("Agg")
matplotlib.pyplot.switch_backend("Agg")


class Test(unittest.TestCase):
    def test_cantilever_beam(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import CantileverBeam

        ndim = 3
        problem = CantileverBeam(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        x[:, 0] = np.linspace(0.01, 0.05, num)
        x[:, 1] = 0.5
        x[:, 2] = 0.5
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_mixed_cantilever_beam(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from smt.problems import MixedCantileverBeam
        from smt.utils.kriging import XSpecs
        from smt.applications.mixed_integer import (
            MixedIntegerContext,
            MixedIntegerSamplingMethod,
            MixedIntegerKrigingModel,
        )
        from smt.sampling_methods import LHS
        from smt.surrogate_models import (
            KRG,
            XType,
            XRole,
            MixIntKernelType,
        )

        problem = MixedCantileverBeam()

        n_doe = 100
        xtypes = [(XType.ENUM, 12), XType.FLOAT, XType.FLOAT]
        xlimits = np.array(
            [
                list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]),
                list([10.0, 20.0]),
                list([1.0, 2.0]),
            ],
            dtype=object,
        )
        xspecs = XSpecs(xtypes=xtypes, xlimits=xlimits)

        sampling = MixedIntegerSamplingMethod(
            LHS,
            xspecs,
            criterion="ese",
        )
        xdoe = sampling(n_doe)
        y = problem(xdoe)

        plt.scatter(xdoe[:, 0], y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_hier_neural_network(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from smt.problems import HierarchicalNeuralNetwork
        from smt.utils.kriging import XSpecs
        from smt.applications.mixed_integer import (
            MixedIntegerContext,
            MixedIntegerSamplingMethod,
            MixedIntegerKrigingModel,
        )
        from smt.sampling_methods import LHS
        from smt.surrogate_models import (
            KRG,
            XType,
            XRole,
            MixIntKernelType,
        )

        problem = HierarchicalNeuralNetwork()

        n_doe = 100
        xlimits = [
            [1, 3],  # meta ord
            [-5, -2],
            [-5, -1],
            ["8", "16", "32", "64", "128", "256"],
            ["ReLU", "SELU", "ISRLU"],
            [0.0, 5.0],  # decreed m=1
            [0.0, 5.0],  # decreed m=2
            [0.0, 5.0],  # decreed m=3
        ]
        xtypes = [
            XType.ORD,
            XType.FLOAT,
            XType.FLOAT,
            XType.ORD,
            (XType.ENUM, 3),
            XType.ORD,
            XType.ORD,
            XType.ORD,
        ]
        xroles = [
            XRole.META,
            XRole.NEUTRAL,
            XRole.NEUTRAL,
            XRole.NEUTRAL,
            XRole.NEUTRAL,
            XRole.DECREED,
            XRole.DECREED,
            XRole.DECREED,
        ]
        xspecs = XSpecs(xtypes=xtypes, xlimits=xlimits, xroles=xroles)
        sampling = MixedIntegerSamplingMethod(
            LHS,
            xspecs,
            criterion="ese",
        )
        xdoe = sampling(n_doe)
        y = problem(xdoe)

        plt.scatter(xdoe[:, 0], y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_robot_arm(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import RobotArm

        ndim = 2
        problem = RobotArm(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        x[:, 0] = np.linspace(0.0, 1.0, num)
        x[:, 1] = np.pi
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_rosenbrock(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import Rosenbrock

        ndim = 2
        problem = Rosenbrock(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        x[:, 0] = np.linspace(-2, 2.0, num)
        x[:, 1] = 0.0
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_sphere(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import Sphere

        ndim = 2
        problem = Sphere(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        x[:, 0] = np.linspace(-10, 10.0, num)
        x[:, 1] = 0.0
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_branin(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import Branin

        ndim = 2
        problem = Branin(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        x[:, 0] = np.linspace(-5.0, 10.0, num)
        x[:, 1] = np.linspace(0.0, 15.0, num)
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_lp_norm(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import LpNorm

        ndim = 2
        problem = LpNorm(ndim=ndim, order=2)

        num = 100
        x = np.ones((num, ndim))
        x[:, 0] = np.linspace(-1.0, 1.0, num)
        x[:, 1] = np.linspace(-1.0, 1.0, num)
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_tensor_product(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import TensorProduct

        ndim = 2
        problem = TensorProduct(ndim=ndim, func="cos")

        num = 100
        x = np.ones((num, ndim))
        x[:, 0] = np.linspace(-1, 1.0, num)
        x[:, 1] = 0.0
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_torsion_vibration(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import TorsionVibration

        ndim = 15
        problem = TorsionVibration(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        for i in range(ndim):
            x[:, i] = 0.5 * (problem.xlimits[i, 0] + problem.xlimits[i, 1])
        x[:, 0] = np.linspace(1.8, 2.2, num)
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_water_flow(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import WaterFlow

        ndim = 8
        problem = WaterFlow(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        for i in range(ndim):
            x[:, i] = 0.5 * (problem.xlimits[i, 0] + problem.xlimits[i, 1])
        x[:, 0] = np.linspace(0.05, 0.15, num)
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_welded_beam(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import WeldedBeam

        ndim = 3
        problem = WeldedBeam(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        for i in range(ndim):
            x[:, i] = 0.5 * (problem.xlimits[i, 0] + problem.xlimits[i, 1])
        x[:, 0] = np.linspace(5.0, 10.0, num)
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def test_wing_weight(self):
        import numpy as np
        import matplotlib.pyplot as plt

        from smt.problems import WingWeight

        ndim = 10
        problem = WingWeight(ndim=ndim)

        num = 100
        x = np.ones((num, ndim))
        for i in range(ndim):
            x[:, i] = 0.5 * (problem.xlimits[i, 0] + problem.xlimits[i, 1])
        x[:, 0] = np.linspace(150.0, 200.0, num)
        y = problem(x)

        yd = np.empty((num, ndim))
        for i in range(ndim):
            yd[:, i] = problem(x, kx=i).flatten()

        print(y.shape)
        print(yd.shape)

        plt.plot(x[:, 0], y[:, 0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()


if __name__ == "__main__":
    unittest.main()
