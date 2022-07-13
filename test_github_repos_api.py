import requests
import definitions
import logging

class  TestGithubReposAPI:
    EXPECTED_NUMBER_OF_REPOS = 2
    EXPECTED_REPO_NAME = 'api_testing'
    EXPECTED_ELEMENTS = ['name','description','html_url']

    def setup_method(self, test_method):
        self.response = requests.get(definitions.repo_end_point)

    def test_status_is_200(self):
        LOGGER = logging.getLogger(__name__)
        if self.response.status_code != 200:
            LOGGER.info('Status code is ' + str(self.response.status_code))
        assert self.response.status_code == 200

    def test_number_of_repos(self):
        assert len(self.response.json()) == self.EXPECTED_NUMBER_OF_REPOS

    def test_find_repo_in_response(self):
        assert self.EXPECTED_REPO_NAME in str(self.response.json())

    def test_basic_elements_in_response(self):
        LOGGER = logging.getLogger(__name__)
        found = True
        for element in self.EXPECTED_ELEMENTS:
            if not element in str(self.response.json()):
                found = False
                LOGGER.info('Element not found in response: ' + element)
        assert found == True

