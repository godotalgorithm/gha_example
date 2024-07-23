"""
Unit and regression test for the gha_example package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import gha_example


def test_gha_example_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "gha_example" in sys.modules
