FROM python:3.10-alpine3.20

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip
RUN pip install -r requirements.txt

RUN apk --update add fontconfig msttcorefonts-installer
RUN update-ms-fonts
RUN fc-cache -f

RUN apk update && apk add libreoffice

# RUN apt-get update && apt-get -y install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra texlive-lang-cyrillic texlive-lang-greek

COPY . /app

ENTRYPOINT ["python3"]
CMD ["main.py"]