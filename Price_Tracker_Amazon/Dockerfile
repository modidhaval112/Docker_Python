FROM python:3.7
ADD price_tracker.py /
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
COPY price_tracker.py /
CMD [ "python", "../price_tracker.py" ]