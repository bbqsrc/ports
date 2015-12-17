# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	mongodb32
PORTVERSION=	3.2.0
CATEGORIES=	databases net
MASTER_SITES=	https://fastdl.mongodb.org/src/ \
		http://fastdl.mongodb.org/src/ \
		http://download.mongodb.org/src/
DISTNAME=	mongodb-src-r${PORTVERSION}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	NOSQL distributed document-oriented database

# mongodb is AGPLv3, C++ driver is APACHE20
LICENSE=	AGPLv3 APACHE20
LICENSE_COMB=	multi

LIB_DEPENDS=	libpcre.so:${PORTSDIR}/devel/pcre \
		libsnappy.so:${PORTSDIR}/archivers/snappy

ONLY_FOR_ARCHS=	i386 amd64
ONLY_FOR_ARCHS_REASON=	"not yet ported to anything other than i386 and amd64"

OPTIONS_DEFINE=	SSL SASL TEST
OPTIONS_DEFAULT=SSL

SSL_USE=	openssl=yes
SSL_MAKE_ARGS=	--ssl
SASL_MAKE_ARGS=	--use-sasl-client
SASL_LIB_DEPENDS=	libsasl2.so:${PORTSDIR}/security/cyrus-sasl2
TEST_DESC=	Add support for running unit tests (VERY SLOW)
TEST_BUILD_DEPENDS =\
		${PYTHON_PKGNAMEPREFIX}yaml>=3.11:${PORTSDIR}/devel/py-yaml\
		${PYTHON_PKGNAMEPREFIX}pymongo>=3.0:${PORTSDIR}/databases/pymongo

USES=		cpe execinfo python:build scons
MAKE_ARGS=	--prefix=${STAGEDIR}${PREFIX} \
		--use-system-pcre --use-system-snappy \
		--release

USERS=	mongodb
GROUPS=	mongodb

USE_RC_SUBR=	mongod

.include <bsd.port.options.mk>

ALL_TARGET=	core
TEST_TARGET=	unittests

post-install:
.for f in mongo mongod mongoperf mongos mongosniff
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/${f}
.endfor

.if ${PORT_OPTIONS:MTEST}
test: build-depends build
	@cd ${BUILD_WRKSRC} && ${SETENV} ${MAKE_ENV} \
		${MAKE_CMD} ${_MAKE_JOBS} ${MAKE_ARGS} ${TEST_TARGET} &&\
		${PYTHON_CMD} ${BUILD_WRKSRC}/buildscripts/resmoke.py\
		--suites=unittests --jobs=${MAKE_JOBS_NUMBER}
.endif

PORTSCOUT=	limitw:1,even

CPE_PRODUCT=	mongodb

.include <bsd.port.mk>
