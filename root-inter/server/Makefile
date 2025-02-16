HOST=127.0.0.1

all: CA_chain.crt

CA.key:
	openssl genrsa -out CA.key 2048

CA.csr: CA.key
	openssl req -new -key CA.key -out CA.csr \
	  -subj "/C=JP/ST=Tokyo/L=Tokyo/O=MyInterCompany/OU=IT/CN=$(HOST)" \
	  -addext "subjectAltName=DNS:example.com,IP:127.0.0.1"

CA.crt: CA.csr
	openssl x509 -req -in CA.csr -CA ../inter/CA.crt -CAkey ../inter/CA.key -CAcreateserial \
	  -out CA.crt -days 365 -sha256  -extfile ext.cnf -extensions usr_cert

CA_chain.crt: CA.crt
	cat CA.crt ../inter/CA_chain.crt > CA_chain.crt

clean:
	rm -f CA.key CA.csr CA.crt CA_chain.crt