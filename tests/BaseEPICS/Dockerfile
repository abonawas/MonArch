FROM centos:8

RUN dnf -y install epel-release gcc gcc-c++ gcc-toolset-9-make readline-devel perl-ExtUtils-Install git make readline

RUN mkdir /EPICS && cd /EPICS && git clone --recursive https://github.com/epics-base/epics-base.git
RUN cd /EPICS/epics-base && make

ENV EPICS_BASE /EPICS/epics-base
ENV EPICS_HOST_ARCH="linux-x86_64"
ENV PATH ${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}
