FROM fedora:30
MAINTAINER samvaran

RUN dnf -y install ruby-devel ruby git gcc\
    gcc-c++ patch readline readline-devel zlib zlib-devel\
    libyaml-devel libffi libffi-devel openssl-devel make \
    bzip2 autoconf automake libtool bison sqlite-devel redhat-rpm-config\
    && dnf clean all;

EXPOSE 4000

# Simple startup script to avoid some issues observed with container restart
ENV HOME=/root
WORKDIR $HOME

RUN git clone https://github.com/rsk/rsk.github.io rsk

WORKDIR /root/rsk

RUN gem install github-pages

CMD ["jekyll serve"]
