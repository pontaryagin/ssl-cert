HOST = 127.0.0.1

.PHONY: all clean

all: CA.crt

CA.key:
	openssl genrsa -out CA.key 2048

CA.crt: CA.key
	openssl req -x509 -new -nodes -days 365 \
		-key CA.key \
		-out CA.crt \
		-subj "/C=JP/ST=Tokyo/L=Minato/O=MyCompany/CN=127.0.0.1" \
		-extensions v3_req \
		-config openssl.cnf

clean:
	rm -f CA.key CA.crt
