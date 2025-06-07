import pytest
from click.testing import CliRunner
from ppmm.cli import cli

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_help(runner):
    """测试CLI帮助命令"""
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Python Pip Mirror Manager' in result.output

def test_ls_command(runner):
    """测试ls命令"""
    result = runner.invoke(cli, ['ls'])
    assert result.exit_code == 0

def test_current_command(runner):
    """测试current命令"""
    result = runner.invoke(cli, ['current'])
    assert result.exit_code == 0

def test_test_command(runner):
    """测试test命令"""
    result = runner.invoke(cli, ['test'])
    assert result.exit_code == 0