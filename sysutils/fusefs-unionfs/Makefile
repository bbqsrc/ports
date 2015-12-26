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
		man/man8/unionfs-fuse.8.gz

USES=		fuse cmake

CFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

post-patch:
	@${REINPLACE_CMD} "s,share/man,man,g" ${WRKSRC}/man/CMakeLists.txt

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/${PORTNAME}

.include <bsd.port.mk>
