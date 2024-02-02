# QR-Auth

Sample project for QR-Authentication
## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)



## Overview

The project is designed to create a secure access system where a website can only be accessed by scanning a QR code.


### Prerequisites

Before running the project, ensure you have the following installed:

- Python (version 3.6 or higher)
- Git


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-project.git
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```


## Usage

To start the main website and redirected website, use the following command:

```bash
python run.py
 ```

- Access the Main Website
1. Open your web browser and navigate to http://127.0.0.1:5000.
2. Follow the on-screen instructions to scan the generated QR code.

- Access the Redirected Website
1. The redirected website is accessible at http://127.0.0.1:5001.
2. Users can access this website only by scanning the QR code from the main website.

- Stop the Program
To stop the program, press CTRL+C in the terminal where the program is running.
