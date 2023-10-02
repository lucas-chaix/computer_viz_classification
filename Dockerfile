FROM python:3.8.10
EXPOSE 8501
COPY src to_install
COPY Silos_detector.py streamlit_app/Silos_detector.py
COPY pages streamlit_app/pages
COPY data data
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install to_install/
RUN pip install matplotlib
RUN pip install streamlit
RUN pip install st-clickable-images
RUN pip install geopy
RUN pip install scikit-learn
CMD ["streamlit", "run", "streamlit_app/Silos_detector.py"]