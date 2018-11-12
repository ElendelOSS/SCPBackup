FROM python:3.7.0-alpine3.7
ENV http_proxy ${http_proxy}
ENV https_proxy ${https_proxy}
ENV version ${version}

RUN apk update && \
    apk add --no-cache \
    build-base \
    gcc \
    git \
    openssl-dev \
    libffi-dev \
    python-dev

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

LABEL   vendor=Elendel \
        au.com.elendel.scpbckup.version=$version \
        au.com.elendel.scpbackup.license="MIT"

WORKDIR /opt/app
COPY ./src /opt/app/
WORKDIR /opt/app/
ENTRYPOINT ["invoke"]
