# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	pynacl
PORTVERSION=	0.3.0
CATEGORIES=	security devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	PyNaCl-${DISTVERSIONPREFIX}${DISTVERSION}${DISTVERSIONSUFFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Python binding to the Networking and Cryptography (NaCl) library

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

TEST_DEPENDS=	py.test:${PORTSDIR}/devel/py-pytest
LIB_DEPENDS=	libsodium.so:${PORTSDIR}/security/libsodium
BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cffi>0:${PORTSDIR}/devel/py-cffi

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

post-install:
	${STRIP_CMD} ${STAGEDIR}${PYTHON_SITELIBDIR}/nacl/_lib/*.so

do-test:
	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} py.test tests)

.include <bsd.port.mk>
