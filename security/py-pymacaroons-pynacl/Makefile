# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	pymacaroons-pynacl
PORTVERSION=	0.9.3
DISTVERSIONPREFIX=	v
CATEGORIES=	security devel
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Macaroon library for Python

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pynacl>=0.3.0:${PORTSDIR}/security/py-pynacl \
			${PYTHON_PKGNAMEPREFIX}six>=1.8.0:${PORTSDIR}/devel/py-six
TEST_DEPENDS=	tox:${PORTSDIR}/devel/py-tox

USE_GITHUB=     yes
GH_ACCOUNT=     matrix-org
GH_PROJECT=     pymacaroons

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

do-test:
	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} tox -e py${PYTHON_SUFFIX})

.include <bsd.port.mk>
