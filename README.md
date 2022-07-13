# api_testing
This is a simple example of test automation for APIs using python requests and pytest.

The endpoint tested is **repos** from Github API. It lists public repositories for the specified user.
Please check this link for more details: https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user

The test has the following files:
- pytest.ini: this file is used to turn on the logging and also defining its level
- definitions.py: this file is used to store test data, like the url of the end point and the Github user which is the owner of the repositories to be listed.
- test_github_repos_api.py: this is the file with the tests

The tests performed are:
- test_status_is_200: this test checks if response status is 200 (OK)
- test_number_of_repos: this test checks if the number of returned repositories is the expected one 
- test_find_repo_in_response: this test checks if a certain repository can be found in the response
- test_basic_elements_in_response: this test checks if certain repository attributes like name, url and description can be found in the response

To run the test:
- install pytest by running *pip install pytest*
- run *python -m pytest test_github_repos_api.py*


