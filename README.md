# server-self
自己証明書でサーバーを立てるケース

## 証明書の作成
```
make -C server-self
```

## サーバーを立てる
```
uvicorn main:app --host 127.0.0.1 --ssl-keyfile ./server-self/CA.key --ssl-certfile ./server-self/CA.crt
```

# root-inter
## 証明書の作成
```
make -C root-inter
```

## サーバーを立てる
```
uvicorn main:app --host 127.0.0.1 --ssl-keyfile ./root-inter/server/CA.key --ssl-certfile ./root-inter/server/CA_chain.crt
```
