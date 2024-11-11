# syntax=docker/dockerfile:1.4
FROM python:3.10-bookworm

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get -y install libreoffice

# RUN apt-get update && apt-get -y install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra texlive-lang-cyrillic texlive-lang-greek

COPY . /app

ENTRYPOINT ["python3"]
CMD ["main.py"]