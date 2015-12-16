# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	mongodb32-tools
PORTVERSION=	3.2.1
DISTVERSIONPREFIX=	r
CATEGORIES=	databases net

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Tools for MongoDB

LICENSE=	APACHE20

BUILD_DEPENDS=	${LOCALBASE}/bin/go:${PORTSDIR}/lang/go

USE_GITHUB=	yes
GH_ACCOUNT=	mongodb
GH_PROJECT=	mongo-tools
GH_TAGNAME=	17a5573

OPTIONS_DEFINE=	SSL SASL
OPTIONS_DEFAULT=SSL

SSL_USE=	openssl=yes
SASL_LIB_DEPENDS+=	libsasl2.so:${PORTSDIR}/security/cyrus-sasl2

.include <bsd.port.options.mk>

CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

.if ${PORT_OPTIONS:MSSL}
MY_TAGS_ARGS+=	ssl
CPPFLAGS+=	-I${LOCALBASE}/include/openssl
LDFLAGS+=	-lssl -lcrypto
.endif

.if ${PORT_OPTIONS:MSASL}
MY_TAGS_ARGS+=	sasl
.endif

.if defined(MY_TAGS_ARGS)
MY_TAGS=	-tags "${MY_TAGS_ARGS}"
.endif

ONLY_FOR_ARCHS=	i386 amd64
ONLY_FOR_ARCHS_REASON=	"not yet ported to anything other than i386 and amd64"

STRIP=		# Stripping can break go binaries

post-patch:
	@cd ${WRKSRC} ; ${MKDIR} ${WRKSRC}/.gopath/src/github.com/${GH_ACCOUNT} ; \
		${LN} -sf ${WRKSRC} ${WRKSRC}/.gopath/src/github.com/${GH_ACCOUNT}/${GH_PROJECT}

do-build:
.for x in bsondump mongostat mongofiles mongoexport mongoimport mongorestore mongodump mongotop mongooplog
	${SETENV} CGO_CPPFLAGS="${CPPFLAGS}"\
		CGO_CFLAGS="${CFLAGS}"\
		CGO_LDFLAGS="${LDFLAGS}"\
		GOPATH=${WRKSRC}/.gopath:${WRKSRC}/vendor go build\
		-o ${WRKSRC}/bin/${x} ${MY_TAGS}\
		-ldflags "-X github.com/${GH_ACCOUNT}/${GH_PROJECT}/common/options.Gitspec=${GH_TAGNAME}"\
		${WRKSRC}/${x}/main/${x}.go
.endfor

do-install:
.for x in bsondump mongostat mongofiles mongoexport mongoimport mongorestore mongodump mongotop mongooplog
	${INSTALL_PROGRAM} ${WRKSRC}/bin/${x} ${STAGEDIR}${PREFIX}/bin/
.endfor
	${MKDIR} ${STAGEDIR}${DOCSDIR}
.for x in LICENSE.md README.md THIRD-PARTY-NOTICES
	${INSTALL_MAN} ${WRKSRC}/${x} ${STAGEDIR}${DOCSDIR}
.endfor

.include <bsd.port.mk>
