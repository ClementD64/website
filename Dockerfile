FROM python:3-alpine as builder

WORKDIR /app
RUN pip install Jinja2
COPY build.py ./
COPY templates/ templates/
RUN ./build.py

FROM caddy:2-alpine

WORKDIR /app
COPY Caddyfile /etc/caddy/Caddyfile
COPY static/ /app/static/
COPY --from=builder /app/dist/ /app/dist/
