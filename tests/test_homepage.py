import time
import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        # print(actual_links)
        assert expected_links == actual_links, 'Validating Nav Links text'
        elements = homepage_nav.get_nav_links()
        for element in elements:
            element.click()
            time.sleep(1)

