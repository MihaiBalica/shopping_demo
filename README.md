# shopping_demo
Demo automation for https://magento.softwaretestingboard.com/

## Description
This project is a test automation framework for Luma Shop using Selenium and Playwright in Python. 
It includes a basic test case for demo, where you navigate to Pants page on Men's articles and add an item to cart

#### And will record videos in the current directory

## Project Structure
- **pages**: This directory contains page object classes representing different pages of the Luma Shop website.
- **utils**: This directory contains utility modules used in the project, such as logger setup and configuration management.
- **tests**: This directory contains the test cases implemented using pytest framework.
- **.env**: This file contains environment variables used for configuration, such as the Luma Shop URL.
- **requirements.txt**: This file lists all the dependencies required for running the project.
- **Dockerfile**: This file contains instructions to build a Docker image for the project.
- **README.md**: This file provides an overview of the project, its structure, and instructions for running the tests locally.

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables: Create a `.env` file and specify the Luma Shop URL.

## Usage
To run the tests locally:
```
pytest
```

## Additional Notes
- Make sure to have Chrome and/or Chromium browser installed on your system for running the tests.
- For running tests in headless mode, modify line 14 in `conftest.py`
```python
        browser = p.chromium.launch(headless=True, executable_path="/opt/google/chrome/chrome")
```
