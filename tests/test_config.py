import pytest
from unittest.mock import patch, MagicMock
from ppmm.core import (
    get_mirrors,
    add_mirror,
    remove_mirror,
    rename_mirror,
    get_current_mirror,
)

@pytest.fixture
def mock_mirrors():
    return {
        'test1': 'https://test1.example.com',
        'test2': 'https://test2.example.com'
    }

def test_get_mirrors(mock_mirrors):
    """测试获取镜像列表"""
    with patch('ppmm.config.mirrors', mock_mirrors):
        mirrors = get_mirrors()
        assert mirrors == mock_mirrors
        assert len(mirrors) == 2

def test_add_mirror(mock_mirrors):
    """测试添加镜像"""
    with patch('ppmm.config.mirrors', mock_mirrors.copy()):
        with patch('ppmm.config.save_config'):
            add_mirror('test3', 'https://test3.example.com')
            mirrors = get_mirrors()
            assert 'test3' in mirrors
            assert mirrors['test3'] == 'https://test3.example.com'

def test_remove_mirror(mock_mirrors):
    """测试删除镜像"""
    with patch('ppmm.config.mirrors', mock_mirrors.copy()):
        with patch('ppmm.config.save_config'):
            remove_mirror('test1')
            mirrors = get_mirrors()
            assert 'test1' not in mirrors

def test_rename_mirror(mock_mirrors):
    """测试重命名镜像"""
    with patch('ppmm.config.mirrors', mock_mirrors.copy()):
        with patch('ppmm.config.save_config'):
            rename_mirror('test1', 'new_test1')
            mirrors = get_mirrors()
            assert 'new_test1' in mirrors
            assert 'test1' not in mirrors
            assert mirrors['new_test1'] == 'https://test1.example.com'

def test_get_current_mirror():
    """测试获取当前镜像"""
    mock_result = MagicMock()
    mock_result.stdout = 'https://test1.example.com\n'
    mock_result.stderr = ''
    with patch('subprocess.run', return_value=mock_result):
        result = get_current_mirror()
        assert result.stdout.strip() == 'https://test1.example.com'