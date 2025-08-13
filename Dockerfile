
FROM alpine:3.16 AS builder

RUN apk add --no-cache \
    bash \
    curl \
    jq \
    python3 \
    py3-pip \
    wget

WORKDIR /app

COPY . /app

RUN chmod +x ./generate.sh && ./generate.sh

FROM httpd:2.4-alpine

WORKDIR /usr/local/apache2/htdocs

COPY --from=builder /app/generated_artifacts/ /usr/local/apache2/htdocs/


EXPOSE 8090


RUN sed -i 's/Listen 80/Listen 8090/' /usr/local/apache2/conf/httpd.conf

CMD ["httpd-foreground"]
