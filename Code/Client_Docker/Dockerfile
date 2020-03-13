FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD Socket_Client.py /Project/Code/
ADD requirements.txt /Project/Code/
WORKDIR /Project/Code/
VOLUME /Project/Data/
RUN pip install -r requirements.txt
CMD [ "python", "Socket_Client.py" ]