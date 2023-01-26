
# VPN


## VPN protocol 종류
https://ko.vpnmentor.com/blog/different-types-of-vpns-and-when-to-use-them/
- PPTP
  - 일반적인 VPN
  - 보안이 없음, 보안을 위해 추가적으로 PPP등의 프로토콜에 의존.
  - 보안이 없어, 가장 빠름
  - 맥이나. 구글 클라우드 등에서 더이상 사용 못하게 함
- Site-to-Site
  - 기업내 VPN등 네트워크와 네트워크를 연결 시켜주는 VPN
  - PPTP와 달리, 라우팅, 암호화 및 암호 해독은 하드웨어 또는 소프트웨어 기반 라우터에 의해 수행
  - open vpn: ssl/tls를 이용한 보안 프로토콜
- L2TP VPN
  - Layer to Tunneling Protocol(레이어 투 터널링 프로토콜)
  - L2TP VPN은 일반적으로 다른 VPN 보안 프로토콜과 결합하여 더 안전한 VPN 연결을 설정하는 VPN
- IPsec
  - Internet Protocol Security
  - 클라이언트를 설치필
  - 모드(전송 모드와 터널링 모드)
  - 