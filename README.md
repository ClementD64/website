# website

```yml
services: 
  caddy:
    build: github.com/ClementD64/website.git#main
    container_name: website
    restart: unless-stopped
    labels: 
      traefik.enable: "true"
      traefik.http.routers.website.entrypoints: https
      traefik.http.routers.website.rule: Host(`clementd.fr`)
      traefik.http.routers.website.tls: "true"
      traefik.http.routers.website.tls.certresolver: prod
      traefik.http.services.website.loadbalancer.server.port: 80
```