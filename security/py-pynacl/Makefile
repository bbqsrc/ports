# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	pynacl
PORTVERSION=	0.3.0
DISTNAME=	PyNaCl-${DISTVERSIONPREFIX}${DISTVERSION}${DISTVERSIONSUFFIX}
CATEGORIES=	security devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Python binding to the Networking and Cryptography (NaCl) library

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libsodium.so:${PORTSDIR}/security/libsodium
BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cffi>0:${PORTSDIR}/devel/py-cffi

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

post-build:
	@${RM} -r ${WRKSRC}/build/temp.*

#post-install:
#	${STRIP_CMD} ${STAGEDIR}${PYTHON_SITELIBDIR}/nacl/*.so

.include <bsd.port.mk>
