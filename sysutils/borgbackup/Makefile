# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	borgbackup
PORTVERSION=	0.29.0
CATEGORIES=	sysutils net
MASTER_SITES=   CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Deduplicating backup program

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${LOCALBASE}/bin/cython:${PORTSDIR}/lang/cython
LIB_DEPENDS=	liblz4.so:${PORTSDIR}/archivers/liblz4
RUN_DEPENDS=	${PYTHON_SITELIBDIR}/msgpack/__init__.py:${PORTSDIR}/devel/py-msgpack-python

USES=		cpe python:3.2+
USE_OPENSSL=	yes
USE_PYTHON=	autoplist distutils

post-install:
.for l in chunker compress crypto hashindex platform_freebsd
	${STRIP_CMD} ${STAGEDIR}${PYTHON_SITELIBDIR}/borg/${l}.so
.endfor

.include <bsd.port.mk>
