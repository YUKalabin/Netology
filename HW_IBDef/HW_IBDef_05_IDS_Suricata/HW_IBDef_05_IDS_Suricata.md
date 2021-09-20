# Мониторинг сетевых событий (Suricata)
В качестве результата пришлите ответы на вопросы в личном кабинете студента на сайте netology.ru.

## Задание 1.
Написать правило для детектирования Xmas-сканирования.

    alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"Xmas_SCAN"; flow:stateless; flags:ASK, FIN, RST, SYN, URG, PSH; classtype:attempted-recon;)

## Задание 2.
Написать правило для детектирования стороннего трафика передающегося службой DNS.

> Сделел два правила для TCP и UDP.

    alert tcp any any <-> any 53 (msg:"Non-DNS"; classtype:inappropriate-content; )
    alert udp any any <-> any 53 (msg:"Non-DNS"; classtype:inappropriate-content; )
    



## Задание 3*.
Написать правило для детектирования файлов документов в сетевом трафике.

> Не нашёл по какому контенту фильтровать.
> А так же не понял к какому типу классов отнести - successful-recon-limited или successful-recon-largescale или attempted-recon

    alert any any any <-> any any (msg:".xls;.doc and other"; content:”|?? ??|”; classtype:???????; )