FROM python:3.10.8-buster

ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

#RUN python -m pip install --upgrade pip

#COPY requirements.txt requirements.txt
#RUN python -m pip install -r requirements.txt

#RUN mkdir /proj_prob
#WORKDIR /proj_prob

#COPY ./proj_prob /proj_prob




RUN mkdir /Serg_site
WORKDIR /Serg_site
COPY requirements.txt /Serg_site/

# RUN apt-get update \
#     && apt-get --yes --no-install-recommends install \
#         python3-dev default-libmysqlclient-dev build-essential \
#         mysql-client libssl-dev \


RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install ez_setup && pip install Pillow && pip install -r requirements.txt
ADD . /Serg_site/