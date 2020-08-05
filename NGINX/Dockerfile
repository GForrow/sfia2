FROM nginx:latest

WORKDIR /etc/nginx/
RUN apt update -y
RUN rm ./conf.d/default.conf
# COPY ./reverse_proxy.conf ./conf.d/
RUN mv reverse_proxy.conf ../sites-available/
RUN ln -s /etc/nginx/sites-available/reverse_proxy.conf sites-enabled/