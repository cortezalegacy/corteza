FROM ubuntu:20.04

ARG CORTEZA_PATH=https://releases.cortezaproject.org/files/corteza-2021.6.0-rc.1-linux-amd64.tar.gz

ENV DEBIAN_FRONTEND "noninteractive"


RUN apt-get update && apt-get install rpm file -y

RUN mkdir -p /root/rpmbuild/BUILD \
             /root/rpmbuild/BUILDROOT \
             /root/rpmbuild/RPMS \
             /root/rpmbuild/SPECS \
             /root/rpmbuild/SOURCES


# TODO: What if $CORTEZA_PATH is local path and get extracted?
ADD $CORTEZA_PATH /root/rpmbuild/SOURCES


WORKDIR /root/rpmbuild
