# Password Generator and Manager

This is a command-line Password Generator and Manager written in Python. The application allows users to create, view, retrieve, and remove passwords stored in CSV files.
## Features

- Generate passwords with specified criteria (number of uppercase letters, lowercase letters, numbers, and symbols).
- Save generated passwords to new or existing CSV files.
- View passwords stored in a CSV file in a tabular format.
- Retrieve passwords by the application name.
- Remove specific passwords from a CSV file.## Requirements

- Python 3.x
- `tabulate` library (for displaying data in tabular format)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/password-generator.git
    cd password-generator
    ```

2. Install the required Python package:

    ```sh
    pip install tabulate
    ```
## Usage

Run the script using Python:

    ```sh
    python password_manager.py
    ```

## Options
1.  Create Password and Add to a New File

    - Prompts for password criteria (number of uppercase, lowercase, numbers, and symbols).
    - Generates a password and saves it to a new file.

2. Create Password and Add to an Existing File

    - Prompts for password criteria (number of uppercase, lowercase, numbers, and symbols).
    - Generates a password and adds it to an existing file.

3. View Password File

    - Displays the content of a specified password file in a tabular format.
4. Retrieve Password

    - Prompts for the application name and retrieves the associated password from the specified file.
5. Remove Password from Existing File

    - Prompts for a password to remove and deletes it from the specified file.
6. Exit

    - Exits the application.

## Example
Here's a brief example of how the application works:

1. Run the script:

    ```sh
    python password_manager.py
    ```
2. Choose an option from the menu (e.g., create a password and add it to a new file).

3. Follow the prompts to enter the required information (e.g., filename, number of uppercase letters, etc.).

4. View the generated password and the updated list of passwords in the file.
## Contributing

Contributions are always welcome!

Please fork the repository and submit a pull request with your changes.


## Author

- [Atharva Ingale](https://github.com/Atharvingale)
