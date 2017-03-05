import mock
import pytest
from ulauncher.search.SortedResultList import SortedResultList
from ulauncher.ext.ResultItem import ResultItem


class TestResultItem(ResultItem):

    def get_name(self):
        return 'test'


class TestSortedResultList:

    @pytest.fixture
    def get_score(self, mocker):
        get_score = mocker.patch('ulauncher.search.SortedResultList.get_score')
        get_score.return_value = 0
        return get_score

    @pytest.fixture
    def res_list(self):
        return SortedResultList('bro', min_score=40, limit=3)

    def result_item(self):
        return TestResultItem()

    def test_append_uses_get_score(self, res_list, get_score):
        ri1 = self.result_item()
        get_score.return_value = 41
        res_list.append(ri1)
        assert ri1 in res_list

        ri2 = self.result_item()
        get_score.return_value = 12
        res_list.append(ri2)
        assert ri2 not in res_list

    def test_append_maintains_limit(self, res_list, get_score):
        get_score.return_value = 50

        ri1 = self.result_item()
        res_list.append(ri1)
        assert len(res_list) == 1
        assert ri1 in res_list

        ri2 = self.result_item()
        res_list.append(ri2)
        assert len(res_list) == 2
        assert ri2 in res_list

        get_score.return_value = 42
        ri3 = self.result_item()
        res_list.append(ri3)
        assert len(res_list) == 3
        assert ri3 in res_list

        ri4 = self.result_item()
        get_score.return_value = 39
        res_list.append(ri4)
        assert len(res_list) == 3
        assert ri4 not in res_list  # doesn't get appended because 39 < min_score /40/

        ri5 = self.result_item()
        get_score.return_value = 100
        res_list.append(ri5)
        assert len(res_list) == 3
        assert ri5 in res_list
        assert ri3 not in res_list  # ri3 gets removed because of the lowest score (42)

        get_score.return_value = 80
        ri6 = self.result_item()
        res_list.append(ri6)
        assert len(res_list) == 3
        assert ri6 in res_list

        assert res_list[0] == ri5  # ri5 stays first, because it has the highest score (100)
