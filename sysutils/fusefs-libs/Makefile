# Created by: Anish Mistry
# $FreeBSD: head/sysutils/fusefs-libs/Makefile 387677 2015-05-27 19:32:08Z delphij $

PORTNAME=	fusefs
PORTVERSION=	2.9.4
CATEGORIES=	sysutils
PKGNAMESUFFIX=	-libs
DISTNAME=	fuse_2_9_4
DISTVERSION=	${DISTNAME}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	FUSE allows filesystem implementation in userspace

OPTIONS_DEFINE=	DOCS

LICENSE=	LGPL21
LICENSE_FILE=	${WRKSRC}/COPYING.LIB

USE_GITHUB=	yes
GH_ACCOUNT=	libfuse
GH_PROJECT=	libfuse

GNU_CONFIGURE=	yes
CONFIGURE_ENV=	MOUNT_FUSE_PATH=${PREFIX}/sbin
CONFIGURE_ARGS=	--prefix=${PREFIX} \
		--with-pkgconfigdir=${PREFIX}/libdata/pkgconfig
INSTALL_TARGET=	install-strip
USES=		iconv libtool autoreconf gettext
USE_LDCONFIG=	yes

PORTDOCS=	*

#pre-build:
#	(@${SH} -c "cd ${WRKSRC} && ./makeconf.sh")

pre-configure:
	${CP} ${LOCALBASE}/share/gettext/config.rpath ${WRKSRC}

post-install:
	${INSTALL_DATA} ${WRKSRC}/include/fuse_kernel.h ${STAGEDIR}${PREFIX}/include/fuse
	@${MKDIR} ${STAGEDIR}${DOCSDIR}/libs
	${INSTALL_DATA} ${WRKSRC}/doc/how-fuse-works ${WRKSRC}/doc/kernel.txt ${STAGEDIR}${DOCSDIR}/libs

.include <bsd.port.pre.mk>

.if ${OPSYS} == DragonFly
IGNORE=	fusefs has not been implemented on DragonFly
.endif

.include <bsd.port.post.mk>
