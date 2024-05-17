# VehicleDiary Flask WebApp

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-project.git
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Download the config file from Google Drive:**
   
   [Google Drive Link](https://drive.google.com/drive/folders/1xEvN9rDsaC7lrbzmM-zMIhWT4JLEr6ua?usp=sharing&pli=1)

6. **Move the config file to the repository folder.**

## Usage

To start the main website, use the following command:

```bash
python run.py
```

## Troubleshooting

If you encounter any issues during installation or usage, feel free to reach out to us for assistance.

## Project Documentation

### Database Setup

## Setting Up a Local Database for the VehicleDiary Flask WebApp

### Prerequisites

- Ensure that you have Python and MySQL installed on your system.
- Have a text editor and terminal/console available for executing commands.

### Steps

1. **Clone the Repository:**

    First, clone the repository containing the project code:

    ```bash
    git clone https://github.com/your-username/your-project.git
    ```

2. **Navigate to the Project Directory:**

    Open a terminal and change your current directory to the project folder:

    ```bash
    cd your-project
    ```

3. **Install Dependencies:**

    Set up a virtual environment (optional but recommended) and install the project dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Activate the virtual environment
    pip install -r requirements.txt
    ```

4. **Create a MySQL Database:**

    Use your preferred MySQL client or command line to create a new database for the project. You can name it `vehiclediary` or choose any suitable name:

    ```sql
    CREATE DATABASE vehiclediary;
    ```

5. **Import the Database Schema:**

    Locate the SQL script provided with the project (e.g., `database_schema.sql`) and execute it in your MySQL client or command line to create the necessary tables (`Vehicle`, `VehicleDiaryEntry`):

    ```bash
    mysql -u your_username -p vehiclediary < database_schema.sql
    ```

    You'll be prompted to enter your MySQL password.

6. **Configure Database Connection:**

    Update the database connection details in the project's configuration file (`config.py`). Ensure that the `SQLALCHEMY_DATABASE_URI` variable points to your local MySQL database:

    ```python
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/vehiclediary'
    ```

    Replace `username` and `password` with your MySQL credentials.

7. **Verify Database Setup:**

    You can verify that the database setup was successful by running the Flask application. Navigate to the project directory and start the application:

    ```bash
    python run.py
    ```

    If the application starts without errors, it indicates that the database connection is established correctly.

### Conclusion

You've now successfully set up a local MySQL database to run the VehicleDiary Flask WebApp. You can start exploring the application and its features locally. If you encounter any issues during setup or usage, refer to the troubleshooting section or seek assistance from the project contributors.
### Web Hosting

1. **Choose a Hosting Provider:**

    - Select a web hosting provider that supports Python and Flask applications.

2. **Deploy the Application:**

    - Upload the project files to your hosting server.
    - Configure the server to run the Flask application.

## Issues with External Project Group

During the development process, our project encountered challenges when collaborating with another project group. Their database structure did not meet the standards required for seamless integration, causing delays and complications in achieving our project goals. We navigated through these challenges by communicating effectively and finding alternative solutions to ensure the success of our project. But due to the challenges we have had to drop newer versions of the project where additional features including:
    - Dynamic list of vehicles
    - Any kind of real flexibility in the code for futurizing

## Contributors

- [Otso Himanen](https://github.com/sineticode)
- [Akseli Närhi](https://github.com/narhiakseli)
