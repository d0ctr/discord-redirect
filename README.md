Discord Link Redirect
===================

Usage
----------------------

To open a Discord link using this application, follow these steps:

1.  Replace the domain part in your Discord URL to `dr.bldbr.club`. For example, change `https://discord.com/channels/@me` to `https://dr.bldbr.club/channels/@me`.
2.  On the web interface, you'll see two buttons:
    *   **Open in browser**: Click this button to open the Discord link in your web browser.
    *   **Open in Discord**: Click this button to open the Discord link in the desktop Discord application (if installed).

Alternatively, you can also access the Discord links directly using the following routes:

*   To open a Discord link in the Discord app: `https://dr.bldbr.club/a/<path>`. For example, `https://discord.com/channels/@me` to `https://dr.bldbr.club/a/channels/@me`.

About
-----

Discord Link Redirect is a Flask web application that provides a convenient way to open Discord links either in a web browser or in the desktop Discord application. It also includes basic input validation to prevent malicious links from being accessed.


Features
--------

*   Open Discord links in a web browser
*   Open Discord links in the desktop Discord application (if installed)
*   Input validation to prevent malicious links

Installation
------------

1.  Clone the repository:
```
    git clone https://github.com/your-username/discord-link-opener.git
```
2.  Navigate to the project directory:
```
    cd discord-link-opener
```
4.  Create a virtual environment (optional but recommended):
```
    python -m venv venv
```
5.  Activate the virtual environment:

On Windows:
```
    venv\Scripts\activate.ps1
```
On Unix or Linux:
```
    source venv/bin/activate
```
5.  Install the required dependencies:
```
    pip install -r requirements.txt
```

Running
-----

1.  Set the `PORT` environment variable to the desired port number:

On Windows:
```
    set PORT=5000
```
On Unix or Linux:
```
    export PORT=5000
```
2.  Run the application:
```
    ./start.sh
```
3.  Open your web browser and visit one of the following routes:

*   To open a Discord link in the browser: `http://localhost:5000/b/<link>`
*   To open a Discord link in the desktop Discord app: `http://localhost:5000/a/<link>`
*   To access the web interface: `http://localhost:5000/<link>`

Replace `<link>` with the desired Discord link (e.g., `channels/1234567890/1234567890`).
Or simply replace the domain, for example if running locally you can change `https://discord.com/channels/@me` to `http://localhost:5000/channels/@me` and it will take you to web interface.

Contributing
------------

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
-------

This project is licensed under the [MIT License](LICENSE).
