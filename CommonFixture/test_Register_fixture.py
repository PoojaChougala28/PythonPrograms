import pytest
def test_success_registe(openlink):
    print("Registed successfully")
#Skipping the function
@pytest.mark.skip
def test_fail_register():
    print("Register failed")