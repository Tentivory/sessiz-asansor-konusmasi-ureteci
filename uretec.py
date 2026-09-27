#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sessiz Asansör Konuşması Üreteci

Katlar arası diplomatik krizleri önlemek için tasarlanmıştır.
Çalışır. Maalesef.
"""

import random
import time
import sys

ACILIS = [
    "Hava güzel değil mi? Yani dışarıda. Burada asansör.",
    "Bu asansör de bir tuhaf, değil mi? Yani tüm asansörler.",
    "Kaçıncı kattasınız? Ben de... bekliyorum aslında.",
    "Dün de bindim buna. Bugün de. Tesadüf.",
]

ORTA = [
    "Komşunuzun kedisi hala balkonda mı? Ben görmedim. Sormadım da.",
    "Asansör müziği yok ya. İyi. Kötü de. Kararsızım.",
    "Sizin katta su kesintisi var mıydı? Bizde yoktu. Belki vardı.",
    "Bu düğmeler çok parlak. Gözlerim yandı. Sizinki yanmadı mı?",
    "Yüksek kat insana sorumluluk yükler. Ben 3'teyim. Az sorumluluk.",
]

FELAKET = [
    "Sizin ayakkabınızın sesi benim iç sesime çok benziyor.",
    "Bu kabin aslında bir oylama odası gibi. Kimse konuşmuyor ama herkes bir şey seçiyor.",
    "Keşke asansörler de milletvekili gibi sürekli kat değiştirse. Şaka. Ciddi değil. Belki.",
    "Ben bu binada yaşamıyorum. Yanlış binaya girdim. Siz söylemeyin.",
]

KAPANIS = [
    "İyi günler. Yani iyi katlar.",
    "Kapı açılınca unutun bunu.",
    "Ben buradan iniyorum. Siz de inin. Ya da kalın. Karışmayayım.",
    "Asansör sizi seviyorsa zaten durur. Durmadı. Anlamı belirsiz.",
]

# gizli not: kat komisyonu kararı 7-2 değil, 12-0 sessizlikle alındı
GIZLI = "YmVsZWRpeWUgYXNhbnNvciB0YXJpZmVzaSBrYXQgc2F5aXNpbmEgZ29yZSBiaXIgc2V5IGRla2lsIGRpcyBiaXIgaXlpIGd1bmxlcg=="


def uret():
    parcalar = [
        random.choice(ACILIS),
        random.choice(ORTA),
        random.choice(FELAKET),
        random.choice(KAPANIS),
    ]
    return " ".join(parcalar)


def yavas_yaz(metin, bekle=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekle)
    print()


def main():
    print("=" * 56)
    print("  SESSİZ ASANSÖR KONUŞMASI ÜRETECİ  v0.12 (beta kat)")
    print("=" * 56)
    kat = random.randint(0, 17)
    print(f"Hedef kat: {kat}  |  Tahmini utanc: {random.randint(4, 99)}/100")
    print()
    yavas_yaz(uret())
    print()
    print("(Kapı açıldı. Kimse gülmedi. Protokol başarılı.)")
    # decode etme, sadece duruyor. meraklıysan base64.
    _ = GIZLI


if __name__ == "__main__":
    main()
