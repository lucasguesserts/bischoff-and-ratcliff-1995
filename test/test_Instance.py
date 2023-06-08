import bischoff_and_ratcliff_1995 as br95

import pandas as pd


def test_case_1():
    actual = br95.Instance(
        T_c=587 * 233 * 220,
        n=8,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2507305,
    )
    expected = pd.read_csv("test/data/case_1.csv")
    pd.testing.assert_frame_equal(actual.df, expected)
    return


def test_case_2():
    actual = br95.Instance(
        T_c=587 * 233 * 220,
        n=10,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2508405,
    )
    expected = pd.read_csv("test/data/case_2.csv")
    pd.testing.assert_frame_equal(actual.df, expected)
    return


def test_case_3():
    actual = br95.Instance(
        T_c=587 * 233 * 220,
        n=12,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2506505,
    )
    expected = pd.read_csv("test/data/case_3.csv")
    pd.testing.assert_frame_equal(actual.df, expected)
    return


def test_case_4():
    actual = br95.Instance(
        T_c=587 * 233 * 220,
        n=8,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2506105,
    )
    expected = pd.read_csv("test/data/case_4.csv")
    pd.testing.assert_frame_equal(actual.df, expected)
    return


def test_case_5():
    actual = br95.Instance(
        T_c=587 * 233 * 220,
        n=10,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2504605,
    )
    expected = pd.read_csv("test/data/case_5.csv")
    pd.testing.assert_frame_equal(actual.df, expected)
    return


def test_case_6():
    actual = br95.Instance(
        T_c=587 * 233 * 220,
        n=12,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2502605,
    )
    expected = pd.read_csv("test/data/case_6.csv")
    pd.testing.assert_frame_equal(actual.df, expected)
    return
