# rpghelper
A Python-Flask project aiming to create a web-based helper application for playing tabletop RPGs. This basic version will be geared towards Cyberpunk RED and allow the users to create characters which will be displayed on a game scenario map. Each user can move their respective characters while the admin can control all map icons.

## Table of Contents

- [Features](#features)
- [Roadmap](#roadmap)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features:

- **Account Management**: Players can create a new account and log in. GM (admin) can log in and manage created accounts.
- **Character Creation**: Players can create a game character. Each game character has basic health, armor class and icon. The GM can create NPC characters.
- **Character Management**: Each player can manage their own characters. Admin can manage all characters.
- **Game Map**: A basic game map to visualize a game scenario. Players can add and move their own game character around the map. The GM can add and move player & NPC characters and change the health/armor stats off all characters.
- **Game Notes**: Players can add public notes related to the game. The notes are displayed next to the map. The GM can create public and private notes to keep track of the game status.

## Roadmap:

- **Account management** (DONE)
- **Character management** (DONE)
- **Game map** (DONE)
- **Game session** (TODO)
- **Notes** (TODO)
- **GM features** (TODO)

## Testing:

To test the current features follow the steps below. When the map & icon features are added, further testing can be done by logging into the app as different users from multiple browser tabs.

After cloning the repo, create a .env file in the root directory of the project and add a secret key and your local database uri. This project is designed for using PostgreSQL, so the .env would look something like this:

```bash
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=postgresql://your-username:your-password@localhost:your-port-number/your-database
```

The easy way to generate a secret key is using the Python interpreter and copying the resulting key to your .env file:

```bash
python ###or python3

import os
print(os.urandom(24))
```

Should you so desire, create and activate a new Python virtual environment. Make sure you are in the /src folder.

```bash
python3 -m venv venv
source venv/bin/activate
```

Create and to connect to your postgresql database, run the following command.

```
flask db init
```

If you have already started testing the app with a previous iteration, run

```bash
flask db upgrade
```

For help on installing and using PostgreSQL, visit the official website at https://www.postgresql.org.

To test the app install the necessary dependencies and start the development server. Make sure you are in the /src directory of the project. By default the app can be found at http://127.0.0.1/5000.

```bash
pip install -r requirements.txt
flask run
```

## Contributing

### Opening Issues

We encourage you to open issues for:

- Reporting bugs
- Requesting new features
- Discussing improvements
- Asking questions

Please make sure to follow these guidelines when opening an issue:

1. **Search Before You Post**: Before opening a new issue, please search existing issues to check if your topic has already been discussed or reported.

2. **Be Descriptive**: Provide a clear and detailed description of the issue or suggestion you have in mind. Include relevant information such as your operating system, browser, or any error messages.

3. **Respect Our Time**: Please be patient when waiting for a response. We are volunteers and will do our best to address your concerns promptly.

### Collaboration and Pull Requests

While we value and appreciate contributions from the community, we currently do not accept direct collaborations or pull requests in this repository. If you'd like to contribute code, please consider forking the repository and working on your changes there. You can then submit a pull request to discuss your changes.

Thank you for understanding and for your interest in improving this project!

## License

This project is licensed under the [MIT License](LICENSE.txt). See the [LICENSE](LICENSE) file for details.
