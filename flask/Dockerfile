FROM python:3.9

ARG ROOT_PATH

RUN mkdir -p $ROOT_PATH
WORKDIR $ROOT_PATH
RUN apt-get update && apt-get install -y libgeos-dev libproj-dev liblapack-dev libblas-dev gfortran
COPY requirements.txt $ROOT_PATH
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt 

COPY . $ROOT_PATH/
CMD [ "tail", "-f", "/dev/null" ]