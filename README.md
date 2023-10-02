# How to use - Docker style (recommended)

```docker build .``` <br/>
```docker run image_id``` <br/>

This will return a Network URL you can follow to access the Streamlit app

# How to use - virtual env (developer mode)

Disclaimer : you might run into dependencies and/or versions problems depending on your version of Python. <br/>
This was tested on Python 3.8.10 (native on Ubuntu 20.04.5 LTS / focal)

First make sure you don't have any virtual environment called .venv hanging in there <br/>
```make clean-venv``` <br/>

Then clean the repo to make sure the build will incorporate your changes, if any <br/>
```make clean-repo``` <br/>

Create a new virtual environment and activate it <br/>
```make init-venv``` <br/>
```source .venv/bin/activate``` <br/>

Install the silos package, and the packages required for the streamlit app <br/>
```pip install src/``` <br/>
```pip install -r requirements.txt``` <br/>

Run the app <br/>
```streamlit run Silos_detector.py```