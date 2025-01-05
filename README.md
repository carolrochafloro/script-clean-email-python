# Clean e-mail

Script to delete unwanted emails from your inbox.

## Project Description

This script helps you automatically delete unwanted emails from your Gmail inbox based on specified criteria.

## Prerequisites

- Python 3.x
- imaplib library (usually included with Python)
- json library (usually included with Python)

## Configuration

Create a config.json file with your email and password:  
`
{
"email": "your_email@gmail.com",
"password": "your_password"
}`

Create a criteria.json file with a list of unwanted senders:  
`delete = [
"unwanted_sender1@example.com",
"unwanted_sender2@example.com"
]`

## How to Run

Navigate to the directory containing main.py.  
Type python mail.py in the terminal.

## Example Usage

Ensure your config.json and criteria.json files are correctly formatted as shown above. Then, run the script to delete unwanted emails from your inbox.

## Contribution

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License
