"""
Unit and regression test for the gha_example package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import gha_example

import subprocess

def test_gha_example_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "gha_example" in sys.modules

def test_canvas():
    """A simple test that can conditionally fail"""
    assert "Henry David Thoreau" in gha_example.canvas()

def test_main():
    """Cover the command-line use of the Python script"""
    subprocess.run(["python", "../gha_example.py"])    
