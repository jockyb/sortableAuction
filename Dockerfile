FROM python:3.9

#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

COPY auction auction
COPY objects objects
#CMD ["python", "-m", "auction.main"]
CMD ["python", "-m", "auction.main"]
