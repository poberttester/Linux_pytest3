from checks import checkout
import pytest
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


# @pytest.fixture()
# def make_folders():
#     return checkout(f"mkdir {data['folderin']} {data['folderout']} {data['folderext']}", '')

class TestPositive:

    def test_step1(self):
        assert checkout(f"cd {data['folderin']}; 7z a {data['folderout']}/arh1", 'Everything is Ok'), 'test_step1 FAIL'

    def test_step2(self):
        assert checkout(f"cd {data['folderout']}; 7z d arh1.7z", 'Everything is Ok'), 'test_step2 FAIL'


# def test_step2():
#   assert checkout(f'cd {folderext}; 7z u {folderout}/arh1', 'Everything is ok'), 'test_step3 FAIL'

if __name__ == '__main__':
    pytest.main(['-vv'])
