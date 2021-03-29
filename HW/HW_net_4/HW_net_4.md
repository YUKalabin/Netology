# Виртуальные частные сети (VPN)
### 3. Какая версия OpenSSL используется

- library versions: OpenSSL 1.1.1f  31 Mar 2020, LZO 2.10

### 4. Какой алгоритм (и с какой длиной ключа) используется для шифрования

- Cipher 'BF-CBC' initialized with 128 bit key

### 5. Какой алгоритм (и с какой длиной ключа) используется дла HMAC аутентификации

- Using 160 bit message hash 'SHA1' for HMAC authentication 
 
Посмотреть все доступные алгоритмы с помощью команд: sudo openvpn --show-ciphers и sudo openvpn --show-digests соответственно.

Указать конкретные с помощью флага --cipher, например, --cipher AES-128-CBC (или просто --cipher AES128) и --auth, например, --auth SHA256, соответственно (удостоверьтесь, что после указания иных алгоритмов в логе вывод тоже меняется).

### 6. Что будет выведено в консоли сервера (sudo openvpn --ifconfig 10.1.0.1 10.1.0.2 --dev tun --secret vpn.key --cipher AES128 --auth SHA256 --verb 3), если:

### 6.1. Подключиться с клиента командой: sudo openvpn --ifconfig 10.1.0.2 10.1.0.1 --dev tun --remote 10.0.0.1 --secret vpn.key --cipher AES256 --auth SHA256 --verb 3

- cipher final failed

### 6.2. Подключиться с клиента командой: sudo openvpn --ifconfig 10.1.0.2 10.1.0.1 --dev tun --remote 10.0.0.1 --secret vpn.key --cipher AES128 --auth SHA512 --verb 3

- packet HMAC authentication failed