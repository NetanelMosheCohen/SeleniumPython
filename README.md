# Web Test Automation Full Framework - Python | Pytest | Selenium | Allure | Docker

## **The framework contains:**

- Cross-browser support for running tests on 3 different browsers (Chrome, Firefox, Edge):
    - Running locally using webdriver-manager
    - Running on Docker containers using Selenoid
  
- Support for parallel execution
  
- Platform and browser parameterization using config file (json)

- Tests run report and dashboard using Allure (including screenshots)

- Reading test data from external file (ini)

- Logger (including errors, stack trace, logging test steps, etc.)

- Page Object Model design


## **Some screenshots from the project:**

Parallel execution on Chrome Docker containers in Selenoid UI:
![alt text](https://github.com/NetanelMosheCohen/SeleniumPython/blob/master/Selenoid.PNG?raw=true)


Live test execution with VNC inside the container:
![alt text](https://github.com/NetanelMosheCohen/SeleniumPython/blob/master/Docker.PNG?raw=true)


The generated Allure report at the end of the run:
![alt text](https://github.com/NetanelMosheCohen/SeleniumPython/blob/master/Allure.PNG?raw=true)
