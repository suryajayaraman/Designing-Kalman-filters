import numpy as np
from sigmaPoints import MerweSigmaPointGenerator

class UnScentedKalmanFilter:
    def __init__(self, dim_x : int,  dim_z : int, fx : callable, hx : callable,
                 dt : float, points : MerweSigmaPointGenerator, x_mean_fn : callable,
                 z_mean_fn : callable, residual_x : callable, residual_z : callable) -> None:
        
        # validate input variables
        assert dim_x >=1, 'State dimension n must be >= 1'
        assert dim_z >=1, 'Measurement dimension n must be >= 1'
        assert fx is not None and fx is callable, 'fx (motion model) must be callable function'
        assert hx is not None and hx is callable, 'hx (measurement model) must be callable function'

        # data variables
        self.dim_x = dim_x
        self.dim_z = dim_z
        self.dt = dt
        self.sigmaPtGenerator = points 

        # funtion objects
        self.fx = fx
        self.hx = hx
        self.x_mean_fn = x_mean_fn
        self.z_mean_fn = z_mean_fn
        self.residual_x = residual_x
        self.residual_z = residual_z

        # intermediate variables
        self.x = np.zeros(dim_x)
        self.P = np.zeros((dim_x, dim_x))
        self.Q = np.zeros((dim_x, dim_x))
        self.R = np.zeros((dim_z, dim_z))


    def predict(self, u : np.ndarray, *args, **kwargs) -> None:
        """Performs predictions step of Unscented Kalman filter

        Args:
            u (np.ndarray): control input, If defined, the 
            motion model fx must be able to parse these inputs
        """
        # generate sigma points
        sigmaPoints = self.sigmaPtGenerator.sigma_points(self.x, self.P)
        fxSigmaPoints = np.zeros_like(sigmaPoints)

        # pass sigma points through fx
        for pt in range(sigmaPoints.shape[0]):
            fxSigmaPoints[pt] = self.fx(sigmaPoints[pt], u, *args, **kwargs)


if __name__ == "__main__":
    np.set_printoptions(suppress=True)