## Designing Kalman Filters
- Chaptere discusses different examples to give you a start towards implementing your own filters.Notable points on numerical stability.
- [Chapter 8 Notebook](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/08-Designing-Kalman-Filters.ipynb)

## Points to remember

813 REFERENCES

317

8.13 References

Bar-Shalein, Yaakov, et al. Estimation with Applications to Tracking and Navigation John Wiley & Sons, 2001

Points to namember:

→P: 262 20 Pose senser simulation (CV) model. Actions X,25

20 tracking problem. Pg: 262 step 1. Choosing state variably →19.263 Stakz transition Stop2

-> 19: 204. (Step 3) Process noise Dicerete wiener/white 0²=103 = √103 = (10) -3.1x162 +0.03 m/s2- → No control yp Sty hoise

→ Clips / meas for (stepe (: Meas. noise Step 7: Initial conditions (XP).

[os-uncorellated blux and y medscament

99 208 Filler order=digree of highest term / CA=2 | LOV

· system model = design choice. If something cou etravels mostly with conn. vel use orda=1, else it'd be bad choice

19:276-272, 1st, 2nd and oth order (ID) Tracking filter code. B:273 fn to Plot residual: from batch orp dara [ Home Residual: 191274, residual within it bene range, riso mean,) err Hw

not diverging check for each state 19:275-276. Failure of oth order filter to anodel/estimate velocity changes.

Residual seems to diverge even thoug Pest & (converging) Py:2762 and order filter, trying to model small SV as acceleration,

dosely trades voice in moartements, creflected in velocity residual Pg 1279 To county this, if we reduce & Chess treest in mags). Large lag in position residuals (diverging. cannot recover from initialisation) polyfit analogy ( Pa (281) fitting parabola to stiline overfitting Adaptive filler introduction.

I trial using ca model, but 1st onder KF. Filler generally lags behind, for its not able to model acceleration, so if at very measu, noise (Pg: 284-285) close to

URBAN

329

CHAPTER & DESIGNING KALMAN FILTERS

$198 Don't incorporate all meastramento directly, check for outliers Po: 290 Just charking diff to(e) and (=) won't work can initially we'd have From uncertainty- risk of being valid Greas). Need to incorporate (P) alle P9:291 Grating concept. To: 292: mahalanobis distance. He (Z_XP) tj Ulapy

ellipsoidal

1993: Mahalanob's dist. & Euclidean distance but rest in (t) leams (S-1) to incorporate uncatainty. 19:294 & Gate approach. (Rectang gate, Ellipsidal gate navet)

19:245 Practical difficulties of Designing (lar).

(79:295) Evaluating fille performance. When we have GT (NEES) (XXX) [EXTP] = scalar 2/12) if Pis very small, then of even for small error e^, E[E]='n I state dim] ~chi squared distribution 19:296 likelihood fr: Prob ? Übelihood are opposite teams with different

up and op. Hore its measure

Uke Whood = low,

it

of

how likely

means one

mea is given state.

of our assumptions is

@y=2. 3 = HPH TAP 1= 1 expysty / ~ exp

Taking log

on both sides

S L'elihood is v, if valid mods, then filter is not optimal. Ley likelihood is preferred as it more numerically stable. P9:297-298) Helihood intuition.

19:899 Ap model change (eg sleevy and acc. yp) P9:300-304, us and position sensor 2D Tracking example. P9-304-308. GPS uses iterative least squares & state

Commercial GPS already has bF, Opp is fitte opp. The not advisable for us to use that in anotour KF) as our Op which are very late to react to State changes. fettre will • smoothed

Nysan

wrong.

Pq : 309: Non-stationaay process, (AZ) might be defferent. Roset F-Q, and last time. Pq: BM, 312: Sensor fusion different rates, separate FQ, HLR as per each sensor, Sample code for 2 sensors of diff, rates tq: 328-326. Tracking ball in atmosphere. Difficult to model non-lineatus with linear filter. Tuning & with ↑ value gives high weightage to (2) causing fivea to track (2) closely. Better to use non-linear for

Chapter 9

Nonlinear Filtering