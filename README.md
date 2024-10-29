# Syslog

Syslog is a logging protocol used for sending and receiving log messages across a network. This repository contains an implementation of a syslog server and client, designed to handle and manage log messages efficiently.

## Features

- **UDP and TCP Support:** Handle log messages over both UDP and TCP protocols.
- **Configurable Logging Levels:** Filter messages based on severity (e.g., DEBUG, INFO, WARN, ERROR).
- **Log Message Parsing:** Automatically parse and format incoming log messages.
- **Custom Output Formats:** Easily configure output formats (e.g., JSON, plain text).
- **File Storage:** Optionally store logs in a local file for persistent storage.
- **Remote Logging:** Forward logs to a remote syslog server.

## Requirements

- Python 3.6+
- Required libraries: `socket`, `logging`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chaudharysurya14/Syslog.git
   cd syslog
