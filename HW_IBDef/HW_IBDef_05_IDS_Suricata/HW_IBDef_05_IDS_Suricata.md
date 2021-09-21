# Мониторинг сетевых событий (Suricata)
В качестве результата пришлите ответы на вопросы в личном кабинете студента на сайте netology.ru.

## Задание 1.
Написать правило для детектирования Xmas-сканирования.

> Нашёл другое описание Xmas сканирования, подправил флаги.

    alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"Xmas_SCAN"; flow:stateless; flags: FIN, URG, PSH; classtype:attempted-recon;)

## Задание 2.
Написать правило для детектирования стороннего трафика передающегося службой DNS.

> Сделал два правила для TCP и UDP.


    alert tcp any any <-> any 53 (msg:"DNS malformed"; app-layer-event:dns.malformed_data; classtype:inappropriate-content; )
    alert udp any any <-> any 53 (msg:"DNS malformed"; app-layer-event:dns.malformed_data; classtype:inappropriate-content; )
    



## Задание 3*.
Написать правило для детектирования файлов документов в сетевом трафике.

> Не нашёл по какому контенту фильтровать.


    alert TCP any any <-> any any (msg:".xls;.doc and other"; content:”|?? ??|”; classtype:???????; )