# test_line_maker.py

import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, expected_slope", [
    (1, 2, 3, 4, 1),
    (-1, 5, 3, 4, -0.25),
    (-1.5, -1.1, 3, 4, 1.13)
    ])
def test_line_maker(x1, y1, x2, y2, expected_slope):
    from line_maker import calc_slope
    slope = calc_slope(x1, y1, x2, y2)
    assert slope == pytest.approx(expected_slope)


@pytest.mark.parametrize("x1, y1, slope, expected_intercept", [
    (1, 2, 1, 1),
    (-1, 5, -.25, 4.75),
    (-1.5, -1.1, 1.13, 0.6)
    ])
def test_line_maker(x1, y1, x2, y2, expected_intercept):
    from line_maker import calc_intercept
    intercept = calc_intercept(x1, y1, x2, y2)
    assert intercept == pytest.approx(expected_intercept)


@pytest.mark.parametrize("x, slope, intercept, expected_y", [
    (1, 1, 1, 2),
    (-2, -.25, 4.75, 5.25),
    (3, 1.13, 0.6, 3.99)
    ])
def test_line_maker(x, slope, intercept, expected_y):
    from line_maker import calc_y
    y = calc_y(x, slope, intercept)
    assert y == pytest.approx(expected_y)