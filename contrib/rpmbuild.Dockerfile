FROM        centos:7
RUN         yum -y install rpm-build python-setuptools
ENTRYPOINT  ["/usr/bin/rpmbuild","--rebuild"]
