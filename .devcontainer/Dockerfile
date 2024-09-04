FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
ENV USERNAME vscode
ENV FLASK_APP flask_backend
EXPOSE 80


RUN mkdir -p /workspace
RUN chown -R $USERNAME:$USERNAME /workspace
WORKDIR /workspace

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y \
    vim \
    python3 \
    curl \
    python3-pip \
    python-is-python3

RUN pip3 install poetry

USER $USERNAME
COPY . .