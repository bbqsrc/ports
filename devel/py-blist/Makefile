# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	blist
PORTVERSION=	1.3.6
CATEGORIES=	devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Drop-in list replacement with better performance for large lists

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

TEST_TARGET=	test

do-test:
	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} ${PYTHON_CMD} ${PYDISTUTILS_SETUP} ${TEST_TARGET})

post-install:
	${STRIP_CMD} ${STAGEDIR}${PYTHON_SITELIBDIR}/blist/*.so

.include <bsd.port.mk>
