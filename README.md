# Convertinator9000

**Convertinator9000** is a simple Python-QT6 desktop application designed to convert an inputted decimal number to a different base form. This app was developed as a personal tool to assist with calculations in a Digital Circuits course at the University of Calgary.  
- Last modified on **September 20th, 2023**.

![alt text](https://github.com/zzz-Ricky/DigitsConverter---Convertinator9000/blob/main/images/Screenshot%202024-11-20%20171447.jpg?raw=true)

---

## Convertinator9000 Installation Guide

Convertinator9000 is a tool that utilizes Python and QT6 to convert and modify decimal digits. Please follow the instructions below to install and set up the program on your Windows or Linux system.

Instructions are provided for the following operating system distributions:
* **Windows 10, 11**
* **Debian Linux** (Ubuntu, Linux Mint, Tails, Proxmox, Kali Linux, Pardus, TrueNAS SCALE, Astra Linux)
* **Arch Linux** (Arch, EndeavorOS, Garuda, Manjaro, SteamOS, and more)

---

## Prerequisites

Before proceeding with the installation, ensure that you have the following:

- A working **Python 3** installation
- A **command prompt** with administrator privileges (Windows)
- A **terminal** with `sudo` privileges (Linux)

---

## Installation Instructions (Windows)

### 1. Clone the Repository

On a Windows machine, the easiest way to install this repository is by cloning it from GitHub. Open your command prompt or PowerShell window and run the following command:

```bash
git clone https://github.com/zzz-Ricky/DigitsConverter---Convertinator9000
```

This will download the project files to your local machine.  
Alternatively, you can download the repository as a `.zip` file from this page and unzip it wherever you prefer on your system.

### 2. Navigate to the Repository

Once the repository has been cloned, navigate to the directory where the project files are located:

```bash
cd DigitsConverter---Convertinator9000
```

### 3. Install Python Dependencies

To install the required Python dependencies, you'll need to have **Python** and **pip** (Python's package installer) installed. The easiest way to handle the installation is by using the `requirements.txt` file, which lists the necessary packages.

Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the key dependency (`PySide6`) manually by running:

```bash
pip install PySide6
```

### 4. Verify the Installation

After the dependencies are installed, it's always a good idea to verify that everything has been set up correctly. You can do this by running the following command to check for any issues with your Python environment or dependencies:

```bash
pip check
```

If everything is installed correctly, you should see the message:

```
No broken requirements found.
```

If any missing dependencies are listed, install them manually using `pip` and then run the check again.

### 5. Running the Program

Once everything is installed, you can run the Convertinator9000 program by executing the following command from within the project directory:

```bash
python widget.py
```

Alternatively, you can double-click `widget.py` in File Explorer to run the script, if that's more convenient for you.

### 6. (Optional) Remove the Program

If you no longer wish to use the program and want to uninstall it, simply delete the project directory and uninstall the Python dependencies with the following commands:

1. Delete the project directory:

   ```bash
   rmdir /S /Q DigitsConverter---Convertinator9000
   ```

2. Uninstall `PySide6` (if installed via `pip`):

   ```bash
   pip uninstall PySide6
   ```

---

## Installation Instructions (Linux)

### 1. Clone the Repository

First, clone the repository to your local machine. Open your terminal of choice and run the following command:

```bash
git clone https://github.com/zzz-Ricky/DigitsConverter---Convertinator9000
```

### 2. Navigate to the Repository

Once the repository is cloned, change into the project directory:

```bash
cd DigitsConverter---Convertinator9000
```

### 3. Install Python Dependencies

Python comes with a handy package manager called **pip**. We will use it to install the necessary libraries for this project via a `requirements.txt` file.

Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, if you prefer to manually install the dependencies, you can run the following command:

```bash
pip install PySide6
```

This will install the required dependencies (such as `PySide6`) for your Python environment.

**Why is this necessary?**  
`PySide6` is a standard library included with **Qt6**. It allows Python scripts to interact seamlessly with **Qt6**-based frontend applications.

### 4. Verify the Installation

It's a good practice to verify that everything has been installed properly. To do this, perform a quick verification check to ensure that the dependencies have been installed correctly:

```bash
pip check
```

If everything was set up correctly, the command should display:

```
No broken requirements found.
```

If there are any missing dependencies, they will be listed on the screen, and you can install them using `pip`.

### 5. Running the Program

Once everything is installed, you can run the Decimal converter program from inside the project directory with the following command:

```bash
python3 widget.py
```

You can refer to the `--help` display for additional usage instructions.

### 6. (Optional) Remove the Program

If you wish to uninstall the program at any time, you can delete the project directory and uninstall the installed Python dependencies:

```bash
sudo rm -r DigitsConverter---Convertinator9000
pip uninstall PySide6
```

### Notes:

- The location of the `DigitsConverter---Convertinator9000` folder is the same directory where you initially cloned the repository. If you used a fresh terminal session, it is likely located in your home or root directory.
  
---

## Troubleshooting

If you encounter any issues during installation, try the following:

- **Ensure Python and pip are up to date** by running the following commands:
  
  On Ubuntu/Debian-based systems:
  ```bash
  sudo apt update
  ```

  On Arch Linux:
  ```bash
  sudo pacman -Syu
  ```

- If you experience issues with missing dependencies, check the `widget.py`, `ui_form.py`, and `Converterz.py` scripts for incorrect paths or missing dependencies. You can use your favorite IDE to check if any imports are underlined in red, indicating a missing dependency. For example:

  ```python
  from PySide6.QtWidgets import QApplication, QWidget
  ```

  If this import is underlined in red, it suggests that `PySide6` is not installed. To resolve this, ensure that `PySide6` is installed in the correct Python environment. Run:

  ```bash
  pip list
  ```

  If `PySide6` is not listed, you may have installed it in another Python environment (e.g., Anaconda). You can activate the correct environment or reinstall the dependency.

---

## Acknowledgements

This project utilizes the frontend library from the following source:

- **[QT6, Pyside6](https://github.com/qt/qtbase)**

This resource was instrumental in the development of this project.

---

## License

This project is licensed under the **MIT License** - see the `LICENSE` file for details.
