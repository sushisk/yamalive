FROM nginx:alpine

RUN apk update && \
    apk add --no-cache \
        python3 \
        py3-pip \
        ffmpeg \
        bash \
        curl \
        ca-certificates \
        cronie
#ytdlp
RUN python3 -m pip install --break-system-packages --no-cache-dir yt-dlp
WORKDIR /usr/share/nginx/html
COPY html/ /usr/share/nginx/html/
COPY cronfile /var/spool/cron/crontabs/root
RUN chmod 600 /var/spool/cron/crontabs/root
CMD ["sh", "-c", "crond -l 8 && nginx -g 'daemon off;'"]
