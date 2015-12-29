# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	canonicaljson
PORTVERSION=	1.0.0
DISTVERSIONPREFIX=	v
CATEGORIES=	devel
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Canonical JSON

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

TEST_DEPENDS=	py.test:${PORTSDIR}/devel/py-pytest

USE_GITHUB=	yes
GH_ACCOUNT=	matrix-org
GH_PROJECT=	python-canonicaljson

USES=		python
USE_PYTHON=	distutils autoplist

do-test:
	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} py.test)

.include <bsd.port.mk>
