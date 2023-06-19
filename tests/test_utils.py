import pytest
from utils import get_data, last_executed_list, sort_list, mask_card, output
import requests

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_last_executed_list(test_data):
    data = last_executed_list(test_data, 3)
    assert len(data) == 3

def test_sort_list(test_data):
    data = sort_list(test_data)
    assert [x["date"] for x in data] == ['2019-12-08T22:46:21.935582',
 '2018-10-14T08:21:33.419441',
 '2018-09-12T21:27:25.241689',
 '2018-04-04T17:33:34.701093',
 '2018-01-26T15:40:13.413061']

def test_mask_card(test_data):
    data = mask_card(test_data[1]['to'])
    assert data == 'Счет **5907'
    data = mask_card(test_data[2]["from"])
    assert data == 'Visa Platinum 1246 37** **** 3588'

def test_output(test_data):
    assert output(test_data) == True