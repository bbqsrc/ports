# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	cookies
PORTVERSION=	2.2.1
CATEGORIES=	www devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Friendlier RFC 6265-compliant cookie parser/renderer

LICENSE=	MIT

TEST_DEPENDS=	py.test:${PORTSDIR}/devel/py-pytest

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

TEST_TARGET=	test

do-test:
	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} ${PYTHON_CMD} ${PYDISTUTILS_SETUP} ${TEST_TARGET})

.include <bsd.port.mk>
