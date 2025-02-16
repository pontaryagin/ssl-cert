# Makefile for generating intermediate CA certificate

.PHONY: all clean

all: CA_chain.crt

CA.key:
	openssl genrsa -out CA.key 4096

CA.csr: CA.key
	openssl req -new -key CA.key -out CA.csr \
		-subj "/C=JP/ST=Tokyo/L=Tokyo/O=MyInterCompany/OU=IT/CN=MyCA"

CA.crt: CA.csr
	openssl x509 -req -in CA.csr -CA ../root/CA.crt -CAkey ../root/CA.key -CAcreateserial \
	  -out CA.crt -days 1825 -sha256 -extfile ext.cnf -extensions v3_ca

CA_chain.crt: CA.crt
	cat CA.crt ../root/CA.crt > CA_chain.crt

clean:
	rm -f CA.key CA.csr CA.crt CA_chain.crt CA.srl
