FROM nginx
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./vue_js /usr/share/nginx/vue_js

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]