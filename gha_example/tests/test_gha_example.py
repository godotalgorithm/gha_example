"""
Unit and regression test for the gha_example package.
"""

# Import package, test suite, and other packages as needed
import sys

import mock
import pytest

import gha_example

def test_gha_example_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "gha_example" in sys.modules

def test_canvas():
    """A simple test that can conditionally fail"""
    assert "Henry David Thoreau" in gha_example.canvas()
