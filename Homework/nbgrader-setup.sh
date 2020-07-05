# Instructions adapted from https://nbgrader.readthedocs.io/en/latest/user_guide/installation.html 
pipenv install nbgrader jupyterlab
jupyter nbextension install --sys-prefix --py nbgrader --overwrite
jupyter nbextension enable --sys-prefix --py nbgrader
jupyter serverextension enable --sys-prefix --py nbgrader
