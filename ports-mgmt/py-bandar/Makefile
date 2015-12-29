# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	bandar
PORTVERSION=	0.0.0
DISTVERSIONPREFIX=	v
CATEGORIES=	ports-mgmt python
DISTNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Create development overlays for the ports tree

RUN_DEPENDS=	port:${PORTSDIR}/ports-mgmt/porttools \
    		poudriere:${PORTSDIRS}/ports-mgmt/poudriere \
		fusefs-unionfs>=1.0:${PORTSDIR}/sysutils/fusefs-unionfs

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	bbqsrc
GH_PROJECT=	bandar
GH_TAGNAME=	033e07e

USES=		python:3.2+
USE_PYTHON=	distutils autoplist

.include <bsd.port.mk>
