def forSOE (rho, y1, y2):
    t1 = y2 ** 2
    t4 = alpha - 0.1e1 / 0.2e1
    t9 = -1 + beta
    t10 = k ** 2
    t12 = y1 ** 2
    t14 = rho ** 2
    t15 = 0.1e1 / t14
    t17 = t1 * t12 * t10 * t15
    t19 = t17 ** (2 * alpha)
    t23 = t1 ** 2
    t28 = xi ** 2
    t34 = t14 ** 2
    t44 = t17 ** alpha
    t51 = alpha + 0.1e1 / 0.2e1
    return([y2,-y2 * (2 * t1 * (y2 * alpha * rho - t4 * y1) * rho * t9 * t10 * t19 + (-t23 * y1 * beta * t10 * rho + (t10 * (beta * t14 * t28 + 1) * t12 - t34 * t28 * t9) * t1 * y2 - y1 * t10 * rho * t9) * t44 - 2 * t1 * rho * t10 * (rho * (alpha * beta + 0.1e1 / 0.2e1) * y2 - beta * t51 * y1)) / (2 * t1 * t4 * t9 * t19 + 2 * (-beta * t23 / 2 + 0.3e1 / 0.2e1 * beta - 0.3e1 / 0.2e1) * t44 - 2 * t1 * t51 * beta) / y1 * t15 / t10])
def forBC (
  ya1,
  ya2,
  yb1,
  yb2):
    t2 = 2 - 2 * alpha
    t3 = ya2 ** t2
    t5 = 2 * alpha
    t6 = ya1 ** (-t5)
    t7 = k ** (-t5)
    t9 = rho_0 ** 2
    t10 = 0.1e1 / t9
    t11 = t10 ** (-alpha)
    t15 = 2 + 2 * alpha
    t16 = ya2 ** t15
    t17 = -1 + beta
    t19 = ya1 ** t5
    t20 = k ** t5
    t22 = t10 ** alpha
    t25 = ya2 ** 2
    t26 = t25 ** 2
    t29 = yb2 ** t2
    t31 = yb1 ** (-t5)
    t34 = yb2 ** t15
    t36 = yb1 ** t5
    t39 = yb2 ** 2
    t40 = t39 ** 2
    return([-beta * t11 * t3 * t6 * t7 - t16 * t17 * t19 * t20 * t22 + beta * t26 + beta - 1,-beta * t29 * t31 * t7 - t17 * t20 * t34 * t36 + beta * t40 + beta - 1])
import math

def forIntegrand (y1):
    t2 = rho ** 2
    t4 = y1 ** 2
    t6 = k ** 2
    return((2 * (1 - beta) * t2 + 2 * t4 * beta * t6) * math.pi * xi * rho / t6)
