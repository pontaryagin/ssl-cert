.PHONY: all clean

all: CA.crt

CA.key:
	openssl genrsa -out CA.key 2048

# ルートCAの自己署名証明書を作成
CA.crt: CA.key
	openssl req -x509 -new -nodes -key CA.key -sha256 -days 3650 -out CA.crt \
	-subj "/C=JP/ST=Tokyo/L=Tokyo/O=MyCompany/OU=IT/CN=MyRootCA"

clean:
	rm -f CA.key CA.crt CA.srl
