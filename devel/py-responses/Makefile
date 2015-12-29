# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	responses
PORTVERSION=	0.5.0
CATEGORIES=	devel www
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Utility library for mocking out the requests Python library

LICENSE=	APACHE20

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}requests>2.0.0:${PORTSDIR}/www/py-requests \
		${PYTHON_PKGNAMEPREFIX}cookies>0:${PORTSDIR}/www/py-cookies

USES=		python:2.7+
USE_PYTHON=	distutils autoplist

.include <bsd.port.mk>
