from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir))))
from configuration import project_conf
from utilities import utilities


def test_calculate_how_many_pages():
    assert utilities.calculate_how_many_pages(0) == 0
    assert utilities.calculate_how_many_pages(100) == 1
    assert utilities.calculate_how_many_pages(1) == 1
    assert utilities.calculate_how_many_pages(99) == 1
    assert utilities.calculate_how_many_pages(101) == 2
    assert utilities.calculate_how_many_pages(199) == 2
    assert utilities.calculate_how_many_pages(200) == 2
    assert utilities.calculate_how_many_pages(489) == 5
    assert utilities.calculate_how_many_pages(2000) == 20
    assert utilities.calculate_how_many_pages(96325) == 964


def test_get_how_many_symbols_in_sector():
    energy_html = open('./DataForTests/first_page_energy.html', encoding="utf8")
    tech_html = open('./DataForTests/first_page_tech.html', encoding="utf8")
    healthcare_html = open('./DataForTests/first_page_healthcare.html', encoding="utf8")
    assert utilities.get_how_many_symbols_in_sector(BeautifulSoup(energy_html, project_conf.HTML_PARSER)) == 216
    assert utilities.get_how_many_symbols_in_sector(BeautifulSoup(tech_html, project_conf.HTML_PARSER)) == 444
    assert utilities.get_how_many_symbols_in_sector(BeautifulSoup(healthcare_html, project_conf.HTML_PARSER)) == 469


def test_build_url():
    assert utilities.build_url("Energy", 100, 100) ==\
           "https://finance.yahoo.com/screener/predefined/ms_energy?offset=100&count=100"
    assert utilities.build_url("Energy", 200, 100) ==\
           "https://finance.yahoo.com/screener/predefined/ms_energy?offset=200&count=100"
    assert utilities.build_url("Technology", 0, 100) ==\
           "https://finance.yahoo.com/screener/predefined/ms_technology?offset=0&count=100"


