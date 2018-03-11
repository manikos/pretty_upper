#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pretty_upper` package."""

import pytest

from click.testing import CliRunner

from pretty_upper import pretty_upper
from pretty_upper import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pretty_upper.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_validate_word():
    vw = pretty_upper.validate_word

    pytest.raises(TypeError, vw, {})
    pytest.raises(TypeError, "vw({})")
    assert vw('') == ''
    assert vw('α') == 'α'


def test_pu():
    pu = pretty_upper.pu

    assert pu('') == ''
    assert pu('α') == 'Α'
    assert pu('ί') == 'Ι'
    assert pu('α ί') == 'Α Ι'
    assert pu('μενού') == 'ΜΕΝΟΥ'
    
