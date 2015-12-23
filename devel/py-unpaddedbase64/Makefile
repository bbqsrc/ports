# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	unpaddedbase64
PORTVERSION=	1.0.1
DISTVERSIONPREFIX=	v
CATEGORIES=	devel
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Unpadded Base64

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	matrix-org
GH_PROJECT=	python-unpaddedbase64

TEST_DEPENDS=	tox:${PORTSDIR}/devel/py-tox

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

do-test:
	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} tox -e py${PYTHON_SUFFIX})

.include <bsd.port.mk>
