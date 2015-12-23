# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	responses
PORTVERSION=	0.5.0
CATEGORIES=	devel www
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Utility library for mocking out the requests Python library

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}requests>2.0.0:${PORTSDIR}/www/py-requests \
		${PYTHON_PKGNAMEPREFIX}cookies>0:${PORTSDIR}/www/py-cookies

LICENSE=	APACHE20

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

# Tests are currently missing from the source distribution.
#TEST_TARGET=	test
#
#do-test:
#	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} ${PYTHON_CMD} ${PYDISTUTILS_SETUP} ${TEST_TARGET})

.include <bsd.port.mk>
