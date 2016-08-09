#!/bin/sh
basedir="$(cd "$(dirname $0)/../"; pwd)"
cd $basedir

${basedir}/py27/bin/python setup.py bdist_rpm \
    --requires python-docker-py,python-setuptools \
    --conflicts des \
    --provides des

rm -Rf ${basedir}/.tmp
mkdir -p ${basedir}/.tmp

docker run --rm \
    -v "${basedir}/dist:/dist" \
    -v "${basedir}/.tmp:/root/rpmbuild/RPMS/noarch" \
    elcolio/des-rpmbuild $(find dist -regex '.*des.*\.src\.rpm$')

rm -f ${basedir}/dist/*.rpm

mv ${basedir}/.tmp/*.rpm ${basedir}/dist/

rm -Rf ${basedir}/.tmp
