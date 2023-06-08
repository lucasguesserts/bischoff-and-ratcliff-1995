import json

import bischoff_and_ratcliff_1995 as br95

import pandas as pd


def get_expected(case_name):
    expected_df = pd.read_csv(f"test/data/{case_name}.csv")
    with open(f"test/data/{case_name}.json", "r") as file:
        expected_dict = json.load(file)
    return {
        "df": expected_df,
        "dict": expected_dict
    }


def test_case_1():
    actual = br95.Instance(
        C={"length": 587, "width": 233, "height": 220},
        n=8,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2507305,
    )
    expected = get_expected("case_1")
    pd.testing.assert_frame_equal(actual.df, expected["df"])
    assert actual.to_dict() == expected["dict"]
    return


def test_case_2():
    actual = br95.Instance(
        C={"length": 587, "width": 233, "height": 220},
        n=10,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2508405,
    )
    expected = get_expected("case_2")
    pd.testing.assert_frame_equal(actual.df, expected["df"])
    assert actual.to_dict() == expected["dict"]
    return


def test_case_3():
    actual = br95.Instance(
        C={"length": 587, "width": 233, "height": 220},
        n=12,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2506505,
    )
    expected = get_expected("case_3")
    pd.testing.assert_frame_equal(actual.df, expected["df"])
    assert actual.to_dict() == expected["dict"]
    return


def test_case_4():
    actual = br95.Instance(
        C={"length": 587, "width": 233, "height": 220},
        n=8,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2506105,
    )
    expected = get_expected("case_4")
    pd.testing.assert_frame_equal(actual.df, expected["df"])
    assert actual.to_dict() == expected["dict"]
    return


def test_case_5():
    actual = br95.Instance(
        C={"length": 587, "width": 233, "height": 220},
        n=10,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2504605,
    )
    expected = get_expected("case_5")
    pd.testing.assert_frame_equal(actual.df, expected["df"])
    assert actual.to_dict() == expected["dict"]
    return


def test_case_6():
    actual = br95.Instance(
        C={"length": 587, "width": 233, "height": 220},
        n=12,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2502605,
    )
    expected = get_expected("case_6")
    pd.testing.assert_frame_equal(actual.df, expected["df"])
    assert actual.to_dict() == expected["dict"]
    return


def test_case_7():
    # this is the first case of the BR1 instances
    actual = br95.Instance(
        C={"length": 587, "width": 233, "height": 220},
        n=3,
        a=[30, 25, 20],
        b=[120, 100, 80],
        L=2,
        s=2502505,
    )
    expected = get_expected("case_7")
    pd.testing.assert_frame_equal(actual.df, expected["df"])
    assert actual.to_dict() == expected["dict"]
    return
