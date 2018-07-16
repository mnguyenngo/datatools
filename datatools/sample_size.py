z_score = {0.70: 1.04,
           0.75: 1.15,
           0.80: 1.28,
           0.85: 1.44,
           0.92: 1.75,
           0.95: 1.96,
           0.96: 2.05,
           0.98: 2.32,
           0.99: 2.58,
           0.999: 3.29,
           0.9999: 3.89,
           0.99999: 4.42}


def min_sample_size(CI=0.95, MOE=0.05):
    """Calculates the minimum sample size when given the confidence interval
    and margin of error.

    Assumptions:
        * population size is unlimited
        * proportion of population is estimated at 0.5 which is conservative
    """
    z = z_score[CI]
    return (z**2 * 0.5**2 / MOE**2)
