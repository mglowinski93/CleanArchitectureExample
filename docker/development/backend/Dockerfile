FROM python:3.10

RUN \
  apt-get update -y && \
  apt-get install -y apt-utils 2>&1 | grep -v "debconf: delaying package configuration, since apt-utils is not installed"
RUN apt-get install -y --no-install-recommends \
  netcat-traditional \
  tzdata
# netcat - package for nc command
# tzdata - package for setting timezone

WORKDIR /app

CMD ["/tools/run-development.sh"]
