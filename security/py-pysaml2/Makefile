# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	pysaml2
PORTVERSION=	4.0.0
CATEGORIES=	security devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Python implementation of SAML Version 2

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}decorator>0:${PORTSDIR}/devel/py-decorator \
		${PYTHON_PKGNAMEPREFIX}requests>1.0.0:${PORTSDIR}/www/py-requests \
		${PYTHON_PKGNAMEPREFIX}Paste>0:${PORTSDIR}/www/py-paste \
		${PYTHON_PKGNAMEPREFIX}zope.interface>0:${PORTSDIR}/devel/py-zope.interface \
		${PYTHON_PKGNAMEPREFIX}repoze.who>0:${PORTSDIR}/devel/py-repoze.who \
		${PYTHON_PKGNAMEPREFIX}pycrypto>2.5:${PORTSDIR}/security/py-pycrypto \
		${PYTHON_PKGNAMEPREFIX}pytz>0:${PORTSDIR}/devel/py-pytz \
		${PYTHON_PKGNAMEPREFIX}openssl>0:${PORTSDIR}/security/py-openssl \
		${PYTHON_PKGNAMEPREFIX}dateutil>0:${PORTSDIR}/devel/py-dateutil \
		${PYTHON_PKGNAMEPREFIX}six>0:${PORTSDIR}/devel/py-six

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

.include <bsd.port.mk>
