FROM python:3.8-slim
# USER root
COPY [".", "./home"]
WORKDIR /home
# COPY [".", "."]
# USER root
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
# RUN chmod -R 700 ./home
# RUN chmod a+rwx ./home
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt
EXPOSE 5001
RUN apt-get -y update
RUN apt-get -y install curl
# RUN apt-get install -y git
# RUN pip install --upgrade pip
# RUN pip install -r ./home/requirements.txt
# WORKDIR /home