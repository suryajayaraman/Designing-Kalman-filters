
import numpy as np


class MerweSigmaPointGenerator:

    def __init__(self, n : int, alpha : float, beta : int, kappa : float) -> None:
        # validate input variables
        assert n >=1, 'State dimension n must be >= 1'
        
        # data variables
        self.n = n
        self.alpha = alpha
        self.beta = beta
        self.kappa = kappa

        # funtion objects
        self.subtract_x = None

        # intermediate variables
        self.numSigmaPoints = 2*n + 1
        self._lambda  =  self.alpha**2 (self.n + self.kappa) - n

        # weights for means
        self.Wm = np.zeros(self.n)
        self.Wm[0] = self._lambda / (self.n + self._lambda)
        self.Wm[1:] = 1.0 / (2 * (self.n + self._lambda))

        # weights for covariance
        self.Wc = np.zeros(self.n)
        self.Wc[0] = (self._lambda / self._lambda + self.n) + 1 - self.alpha**2 + self.beta
        self.Wc[1:] = 1.0 / (2 * (self.n + self._lambda))


    def sigma_points(self, x : np.ndarray, P : np.ndarray) -> np.ndarray:
        # ensure dimensions match
        assert len(x) == self.n, f'x shape {x.shape} doesnt match state dimension n = {self.n}'
        assert P.shape[0] == self.n, f'x shape {x.shape} doesnt match state dimension n = {self.n}'

        # initialize return variable
        sigmaPoints = np.zeros((self.numSigmaPoints, self.n))
        return sigmaPoints