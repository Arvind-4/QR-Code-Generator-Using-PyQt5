# Generate QR Codes using PyQt5

Generating QR codes using PyQt5 combines the graphical user interface (GUI) capabilities of PyQt5 with the ability to generate QR codes. PyQt5 is a set of Python bindings for the Qt application framework, allowing for the creation of cross-platform applications with rich graphical interfaces.

This guide will walk you through setting up a development environment, cloning a repository, installing necessary dependencies, and running the code to generate QR codes using PyQt5.

## Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.10 or higher
- Git

## Running Locally

Follow these steps to set up and run the QR code generation application on your local machine:

### Step 1: Create a Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus several additional packages. It allows you to manage dependencies for different projects separately.

1. Install `virtualenv` if you haven’t already:

```bash
python3.10 -m pip install virtualenv
```

2.  Navigate to your development directory and create a new directory for the project:

```bash
cd ~/Dev
mkdir qrcode
cd qrcode
```

3.  Create a virtual environment within this directory:

```bash
python3.10 -m virtualenv .
```

4.  Activate the virtual environment:

```bash
source bin/activate
```

After activation, your shell prompt should change to indicate that you are now working within the virtual environment.

### Step 2: Clone Repository and Install Dependencies

You need to clone the repository containing the QR code generation code and install the required Python packages.

1.  Clone the repository from GitHub:

```bash
git clone https://github.com/Arvind-4/qrcode-using-pyqt5.git .
```

2.  Install the required dependencies. The `requirements.txt` file lists the packages needed for the project, and `requirements-dev.txt` may include additional packages needed for development:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

This ensures all necessary libraries are installed in your virtual environment.

### Step 3: Run the Code

With the environment set up and dependencies installed, you can now run the application to generate QR codes.

1.  Execute the main script:

```bash
python run.py
```

This script starts the application, which should open a graphical interface for generating QR codes.

## Summary

By following these steps, you’ve created a virtual environment, set up the project, and run a PyQt5 application to generate QR codes. PyQt5 provides a powerful way to create GUI applications, and combining it with QR code generation functionality allows for the creation of interactive and useful tools.

If you encounter any issues or need further customization, please create an issue on the repository for any problems.
