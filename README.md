# CS-340 Animal Shelter Database

This project was done to keep track of all the animals that come in and out of the shelter. Various attributes are breed, size, weight, name, address (if have owner) and other noted characteristics.
This project was slightly challenging, but particularly fun because I, myself am a dog mom, and love animals.

## Prerequisites

Before running this application, you need to have the following installed:

1. Python 3.6 or higher
2. MongoDB (running on localhost:54319)
3. pip (Python package installer)
4. The following Python packages:
   - pymongo
   - pandas
   - jupyter
   - jupyter-dash
   - dash
   - dash-leaflet
   - plotly
   - numpy
   - matplotlib

### Installing pip

pip comes pre-installed with Python 3.4+ and Python 2.7.9+. If you don't have pip installed, you can install it using the following methods:

#### Windows
1. Download the get-pip.py script: https://bootstrap.pypa.io/get-pip.py
2. Open Command Prompt and navigate to the directory containing the downloaded file
3. Run: `python get-pip.py`

#### macOS
1. Open Terminal
2. If you installed Python with Homebrew: pip is already installed
3. Otherwise, run: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
4. Then run: `python3 get-pip.py`

#### Linux
1. For Debian/Ubuntu: `sudo apt-get install python3-pip`
2. For Fedora: `sudo dnf install python3-pip`
3. For CentOS/RHEL: `sudo yum install python3-pip`

### Verifying pip installation
To verify pip is installed correctly, run:
```bash
pip --version
```
or
```bash
pip3 --version
```

### Installing Required Packages
Once pip is installed, you can install the required Python packages:

```bash
pip install pymongo pandas jupyter jupyter-dash dash dash-leaflet plotly numpy matplotlib
```

If you're using Python 3, you might need to use `pip3` instead of `pip`:

```bash
pip3 install pymongo pandas jupyter jupyter-dash dash dash-leaflet plotly numpy matplotlib
```

### Using Virtual Environments (Recommended)

It's a best practice to use virtual environments for Python projects to avoid package conflicts. Here's how to set up a virtual environment:

#### Windows
```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install packages in the virtual environment
pip install pymongo pandas jupyter jupyter-dash dash dash-leaflet plotly numpy matplotlib
```

#### macOS/Linux
```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install packages in the virtual environment
pip install pymongo pandas jupyter jupyter-dash dash dash-leaflet plotly numpy matplotlib
```

To deactivate the virtual environment when you're done:
```bash
deactivate
```

### Troubleshooting pip

If you encounter issues with pip, try these common solutions:

1. **Permission errors**: If you get permission errors, try:
   - On Windows: Run Command Prompt as Administrator
   - On macOS/Linux: Use `sudo pip install` or install packages for the current user only with `pip install --user`

2. **SSL Certificate errors**: If you get SSL certificate errors:
   ```bash
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
   ```

3. **Outdated pip**: Update pip to the latest version:
   ```bash
   pip install --upgrade pip
   ```
   or
   ```bash
   pip3 install --upgrade pip
   ```

4. **Path issues**: Ensure pip is in your system PATH. You might need to restart your terminal/command prompt after installing pip.

5. **Multiple Python installations**: If you have multiple Python installations, specify which pip to use:
   ```bash
   python3 -m pip install <package_name>
   ```

### Offline Installation

If you're in an environment with limited internet access, you can download packages on a machine with internet access and transfer them:

1. **Download packages on a machine with internet access**:
   ```bash
   pip download -d ./offline_packages pymongo pandas jupyter jupyter-dash dash dash-leaflet plotly numpy matplotlib
   ```

2. **Transfer the entire "offline_packages" directory** to the target machine

3. **Install from the downloaded files**:
   ```bash
   pip install --no-index --find-links=./offline_packages pymongo pandas jupyter jupyter-dash dash dash-leaflet plotly numpy matplotlib
   ```

## Database Setup

The application expects a MongoDB database named 'AAC' with a collection named 'animals'. The database should be accessible with the following credentials:
- Username: MyUserAdmin
- Password: trinidad1

## Running the Application

### Running the Jupyter Notebook Dashboard

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open the `ModuleSixMilestone.ipynb` file in the Jupyter interface.

3. Run all cells in the notebook by clicking on "Cell" in the menu bar and selecting "Run All", or by using the keyboard shortcut Shift+Enter for each cell.

4. The Dash application will start and display a dashboard with interactive features for filtering and viewing animal data.

### Running the Test Script

To test the basic functionality of the database connection and CRUD operations:

```bash
python test_script.py
```

This script creates a new animal record in the database and then reads it back to verify the operation.

## Application Features

- Filter animals by type (Cats/Dogs) using the buttons at the top
- Interactive data table with sorting and filtering capabilities
- Geolocation map showing the location of selected animals
