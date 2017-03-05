import pytest
from ulauncher.search.calc.CalcMode import CalcMode, eval_expr


class TestEvalExpr:

    def test_eval_expr__returns_correct_val(self):
        assert eval_expr('1+1') == 2

    def test_eval_expr__raises_SyntaxError(self):
        with pytest.raises(SyntaxError):
            assert eval_expr('1-+')


class TestCalcMode:

    @pytest.fixture
    def ActionList(self, mocker):
        return mocker.patch('ulauncher.search.calc.CalcMode.ActionList')

    @pytest.fixture
    def RenderResultListAction(self, mocker):
        return mocker.patch('ulauncher.search.calc.CalcMode.RenderResultListAction')

    @pytest.fixture
    def CalcResultItem(self, mocker):
        return mocker.patch('ulauncher.search.calc.CalcMode.CalcResultItem')

    @pytest.fixture
    def mode(self):
        return CalcMode()

    def test_is_enabled(self, mode):
        assert mode.is_enabled('5')
        assert mode.is_enabled('-5')
        assert mode.is_enabled('5+')
        assert mode.is_enabled('(5/0')
        assert mode.is_enabled('0.5/0')
        assert mode.is_enabled('0.5e3+ (11**3+-2^3)')

        assert not mode.is_enabled('+2')
        assert not mode.is_enabled(')+3')
        assert not mode.is_enabled('e3')
        assert not mode.is_enabled('a+b')

    def test_on_query(self, mode, ActionList, RenderResultListAction, CalcResultItem):
        assert mode.on_query('3+2') == ActionList.return_value
        assert mode.on_query('3+2*') == ActionList.return_value
        ActionList.assert_called_with((RenderResultListAction.return_value,))
        RenderResultListAction.assert_called_with([CalcResultItem.return_value])
        CalcResultItem.assert_called_with(result=5)

    def test_on_query__invalid_expr(self, mode, ActionList, RenderResultListAction, CalcResultItem):
        assert mode.on_query('3++') == ActionList.return_value
        ActionList.assert_called_with((RenderResultListAction.return_value,))
        RenderResultListAction.assert_called_with([CalcResultItem.return_value])
        CalcResultItem.assert_called_with(error='Invalid expression')

    def test_on_query__result_is_0__returns_0(self, mode, CalcResultItem):
        mode.on_query('2-2')
        CalcResultItem.assert_called_with(result=0)
