FROM nginx

COPY conf.d /etc/nginx/conf.d
ENTRYPOINT ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]