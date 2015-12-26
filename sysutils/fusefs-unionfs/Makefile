# Created by: Gea-Suan Lin <gslin@gslin.org>
# $FreeBSD: head/sysutils/fusefs-unionfs/Makefile 380917 2015-03-10 14:15:55Z amdmi3 $

PORTNAME=	unionfs
PORTVERSION=	1.0
DISTVERSIONPREFIX=	v
CATEGORIES=	sysutils
PKGNAMEPREFIX=	fusefs-

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	FUSE based implementation of the well-known unionfs

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	rpodgorny
GH_PROJECT=	unionfs-fuse

PLIST_FILES=	bin/unionfs \
		bin/unionfsctl \
		man/man8/unionfs.8.gz

USES=		python:3.2+,test fuse cmake localbase

post-patch:
	@${REINPLACE_CMD} "s,share/man,man,g" ${WRKSRC}/man/CMakeLists.txt

do-test:
	@cd ${WRKSRC} && ${PYTHON_CMD} test.py

post-install:
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/*

.include <bsd.port.mk>
