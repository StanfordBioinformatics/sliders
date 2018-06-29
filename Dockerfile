FROM python:3.6.5-jessie
ENTRYPOINT /bin/bash

RUN pip install sliders==0.2.1

RUN mkdir /test-inputs
COPY sliders/tests/fastqc.json /test-inputs/fastqc.json
COPY sliders/tests/sample_fastqc.data /test-inputs/sample-fastqc.data 
COPY sliders/tests/sample_flagstat.tsv /test-inputs/sample-flagstat.tsv
