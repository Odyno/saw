FROM "python:3.9"
RUN pip install pip --upgrade

WORKDIR /usr/src/app
COPY  . .
RUN pip install --no-cache-dir .

CMD ["/bin/bash"]
