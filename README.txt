Commands to run in the VENV for setup using Conda. Install Anaconda. 
Open Anaconda Prompt

- Create a new VENV and potentially optional python version with it
    conda create -n my_env python=3.6.3 anaconda

-First activate the VENV
    conda activate my_env

- Second, install the version of Python 
    conda install python=X.X.X

- Third, install PySide
    conda install -c conda-forge pyside

- Fourth, install Pyqt
    conda install -c anaconda pyqt