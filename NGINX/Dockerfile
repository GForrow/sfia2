FROM nginx:latest

WORKDIR /etc/nginx/

RUN apt update -y
RUN apt install openssl -y
RUN rm ./conf.d/default.conf

COPY . conf.d/
