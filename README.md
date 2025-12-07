
- Parallel execution + dependencies
    - requirements.txt file - pytest-xdist for parallel, pytest-dependency for test dependencies

- Retry mechanism
    -  pytest-rerunfailures configured in CLI ( pytest.yml file)

- CI/CD integration
     - ✅ Automatically runs tests on pushes and pull requests to main
     - ✅ Runs the workflow on multiple operating systems (Linux, macOS, Windows).
     - ✅ Supports running tests on multiple Python versions (currently just 3.9, but easily extendable).
     - ✅ Sets up the Python environment and installs dependencies, covering environment selection.
     - ✅ Executes tests in parallel (-n auto)
     - ✅ Retries failed tests 2 times (--reruns 2)
     - ✅ Generates JUnit XML reports for CI/CD artifact collection
     - ✅ Uploads test results as artifacts for later inspection or reporting.

