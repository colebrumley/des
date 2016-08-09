#!/bin/sh
basedir="$(cd "$(dirname $0)/../"; pwd)"
cd $basedir

cp ${basedir}/dist/des-*.tar.gz ${basedir}/DEBIAN/

docker run -it --rm -v "$(pwd):/src" -v "$(pwd)/dist:/dest" \
    ubuntu:16.04 dpkg-deb --build /src /dest

rm -f ${basedir}/DEBIAN/des-*.tar.gz
