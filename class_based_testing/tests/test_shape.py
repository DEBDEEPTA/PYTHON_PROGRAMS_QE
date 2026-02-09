import pytest
import  time
import class_based_testing.circle as c
import class_based_testing.rectangle as r


class TestShape:

    def setup_method(self,method):
        print(f"Setting Up Method {method.__name__}")  # RUNS PRIOR EVERY TEST CASES  FUNC.


    def teardown_method(self,method):
        print(f"Tearing Down Method {method.__name__}") # RUNS AFTER EVERY TEST CASE  FUNC.


    @pytest.fixture
    def rectangle_fixture_t1_eg(self):
        result = r.Rectangle(5,6)
        return result.area()

    @pytest.fixture
    def rectangle_fixture_t2_eg(self):
        result = r.Rectangle(7,8)
        return result.area()

    def test_circle(self):

        result = c.Circle(5)
        assert result.area() == 78

    def test_rectangle(self):
        result = r.Rectangle(3,4)
        assert result.area() == 12
    @pytest.mark.xfail
    def test_rectangle_fixture_1(self,rectangle_fixture_t1_eg):
        assert rectangle_fixture_t1_eg == 300 # will fail

    @pytest.mark.slow
    def test_rectangle_fixture_2(self,rectangle_fixture_t2_eg):
        time.sleep(5)
        assert rectangle_fixture_t2_eg == 56




