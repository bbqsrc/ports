# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	pymacaroons-pynacl
PORTVERSION=	0.9.3
DISTVERSIONPREFIX=	v
CATEGORIES=	security devel python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Macaroon library for Python

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pynacl>=0.3.0:${PORTSDIR}/security/py-pynacl \
		${PYTHON_PKGNAMEPREFIX}six>=1.8.0:${PORTSDIR}/devel/py-six
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}nose>0:${PORTSDIR}/devel/py-nose \
		${PYTHON_PKGNAMEPREFIX}hypothesis>0:${PORTSDIR}/devel/py-hypothesis

USE_GITHUB=	yes
GH_ACCOUNT=	matrix-org
GH_PROJECT=	pymacaroons

USES=		python
USE_PYTHON=	autoplist distutils

do-test:
	@(cd ${WRKSRC} && nosetests-${PYTHON_VER})

.include <bsd.port.mk>
