#!/usr/bin/env bash

BUILD_VERSION=${BUILD_VERSION:-"2021.6.0-rc.1"}

ARRAY=(${BUILD_VERSION//-/ })

RPM_VERSION=${ARRAY[0]}
WITHOUT_RPM_VERSION="${BUILD_VERSION/$RPM_VERSION/}"

if [[ "$WITHOUT_RPM_VERSION" == "" ]]; then
  RPM_RELEASE="2"
elif [[ "$WITHOUT_RPM_VERSION" =~ -rc.[0-9]+ ]]; then
  RPM_RELEASE="1.${WITHOUT_RPM_VERSION/-/}"
else
  RPM_RELEASE="0.${WITHOUT_RPM_VERSION/-/}"
fi

ENDPOINT="https://releases.cortezaproject.org/files"


docker build --build-arg CORTEZA_PATH="$ENDPOINT/corteza-$BUILD_VERSION-linux-amd64.tar.gz" -t corteza-rpm .

docker run -v $(pwd)/BUILD:/root/rpmbuild/BUILD \
           -v $(pwd)/RPMS:/root/rpmbuild/RPMS \
           -v $(pwd)/SPECS:/root/rpmbuild/SPECS \
           corteza-rpm rpmbuild -bb --define "_version $BUILD_VERSION" \
                                    --define "_rpm_version $RPM_VERSION" \
                                    --define "_rpm_release $RPM_RELEASE" \
                                    SPECS/corteza.spec
