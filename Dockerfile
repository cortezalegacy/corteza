# build-stage
FROM alpine:3 as build-stage

ARG CORTEZA_SERVER_PATH=https://releases.cortezaproject.org/files/corteza-server-2021.6.0-rc.3-linux-amd64.tar.gz
ARG CORTEZA_WEBAPP_PATH=https://releases.cortezaproject.org/files/corteza-webapp-2021.6.0-rc.3.tar.gz

RUN mkdir /tmp/server
RUN mkdir /tmp/webapp

ADD $CORTEZA_SERVER_PATH /tmp/server
ADD $CORTEZA_WEBAPP_PATH /tmp/webapp

RUN apk update && apk add --no-cache file

RUN file "/tmp/server/$(basename $CORTEZA_SERVER_PATH)" | grep -q 'gzip' && \
    tar zxvf "/tmp/server/$(basename $CORTEZA_SERVER_PATH)" -C / || \
    cp -a "/tmp/server" /

RUN mv /corteza-server /corteza

WORKDIR /corteza

RUN rm -rf /corteza/webapp

RUN file "/tmp/webapp/$(basename $CORTEZA_WEBAPP_PATH)" | grep -q 'gzip' && \
    mkdir /corteza/webapp && tar zxvf "/tmp/webapp/$(basename $CORTEZA_WEBAPP_PATH)" -C /corteza/webapp || \
    cp -a "/tmp/webapp" /corteza/webapp


# deploy-stage
FROM alpine:3

ENV STORAGE_PATH "/data"
ENV CORREDOR_ADDR "corredor:80"
ENV HTTP_ADDR "0.0.0.0:80"
ENV HTTP_WEBAPP_ENABLED "true"
ENV HTTP_WEBAPP_BASE_DIR "/corteza/webapp"
ENV PATH "/corteza/bin:${PATH}"

WORKDIR /corteza

VOLUME /data

COPY --from=build-stage /corteza ./

HEALTHCHECK --interval=30s --start-period=1m --timeout=30s --retries=3 \
    CMD curl --silent --fail --fail-early http://127.0.0.1:80/healthcheck || exit 1

EXPOSE 80

ENTRYPOINT ["./bin/corteza-server"]

CMD ["serve-api"]