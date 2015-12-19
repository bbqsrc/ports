# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	PyNaCl
PORTVERSION=	0.3.0
CATEGORIES=	security devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Python binding to the Networking and Cryptography (NaCl) library

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libsodium.so:${PORTSDIR}/security/libsodium

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

post-build:
	@${RM} -r ${WRKSRC}/build/temp.*

post-install:
	${STRIP_CMD} ${PYTHON_SITELIBDIR}/nacl/*.so

.include <bsd.port.mk>
