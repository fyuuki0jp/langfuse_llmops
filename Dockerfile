FROM mcr.microsoft.com/devcontainers/python:dev-3.12-bookworm
RUN pip install --upgrade pip
RUN pip install uv

RUN apt-get update && apt-get install -y nodejs npm
RUN npm install -g npm yarn