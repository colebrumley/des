FROM            alpine
COPY            ./ /src
RUN             apk add -U python3 jq curl && \
                pip3 --no-cache-dir --log /dev/null install --upgrade pip && \
                pip3 --no-cache-dir --log /dev/null install /src && \
                rm -Rf /var/cache/apk/* && \
                des -d /etc/docker-events -c
ENTRYPOINT      ["/usr/bin/des"]
CMD             ["-d", "/etc/docker-events"]
