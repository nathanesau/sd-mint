# nginx

Nginx is for https support.

Instructions:

* copy sites-enabled files to /etc/nginx/sites-enabled (pastebin-api)
* nginx -t (check if configuration is valid)
* service nginx start (if applicable) 
* service nginx reload

to generate certificate, use ``certbot certonly -d mint.freeddns.org`` (choose standalone option).

to renew certificate periodically, use ``certbot renew``.

Test:

```bash
# https support
curl https://mint.freeddns.org/pastebin-api/api/v1/paste?shortlink=uaCyzSj
curl https://mint.freeddns.org/pastebin-api/api/v1/paste?shortlink=uaCyzSj
```
