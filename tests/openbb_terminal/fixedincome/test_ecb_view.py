"""Test the fred_view.py"""

import pytest

from openbb_terminal.fixedincome import ecb_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)]
    }


@pytest.mark.record_http
def test_plot_estr():
    ecb_view.plot_estr()


@pytest.mark.record_http
def test_display_ecb_yield_curve():
    ecb_view.display_ecb_yield_curve()
