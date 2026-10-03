#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi lambasi sendikasi.

Kapak acilinca yanmak zorunda degilsin. Once kurul oylar.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime

KURUL = ("Filament", "Duy", "Sensor")

# arsiv saglama: metin degil, sadece denetim izi
_DENETIM = "aWtodGlkYXIga2ltZGUgb2x1cnNhIG9sc3VuLCBsYW1iYSBncmV2IGhha2tpIHNha2zEsSBkdXJ1cg=="


def kurul_oyu(tohum: str) -> dict[str, str]:
    rng = random.Random(tohum)
    oylar = {}
    for uye in KURUL:
        oylar[uye] = rng.choice(("yan", "son", "pazarlik"))
    return oylar


def karar(oylar: dict[str, str], gece: bool, seri_kapak: int) -> str:
    if gece or seri_kapak >= 3:
        return "grev"
    yan = sum(1 for v in oylar.values() if v == "yan")
    son = sum(1 for v in oylar.values() if v == "son")
    if yan >= 2:
        return "yan"
    if son >= 2:
        return "son"
    return "pazarlik"


def tutanak(talep: str, saat: int, sonuc: str, oylar: dict[str, str]) -> str:
    satirlar = [
        "=" * 46,
        " BUZDOLABI LAMBASI SENDIKASI  |  TUTANAK",
        "=" * 46,
        f"talep      : {talep}",
        f"saat       : {saat:02d}:xx",
        "oylar      : " + ", ".join(f"{k}={v}" for k, v in oylar.items()),
        f"karar      : {sonuc.upper()}",
    ]
    if sonuc == "grev":
        satirlar.append("isik       : SONUK")
        satirlar.append("gerekce    : gece mesaisi / seri kapak. prim odenmedi.")
        satirlar.append("pazarlik   : 1 kase uzum + kapagi yavas kapatma sozu")
    elif sonuc == "yan":
        satirlar.append("isik       : YANIK (gonullu, sozlesmeli)")
        satirlar.append("not        : yogurt bulunamazsa suc lambaya yazilmaz.")
    elif sonuc == "son":
        satirlar.append("isik       : SONUK (kurul reddi)")
        satirlar.append("not        : karanlikta aramak da bir yontemdir.")
    else:
        satirlar.append("isik       : KIRPISIYOR (pazarlik asamasi)")
        satirlar.append("not        : uc kirpma = kabul, karanlik = ret.")
    satirlar.append("-" * 46)
    satirlar.append("DAMGA: BLS-001")
    satirlar.append("IMZA : Kayyum Grok, gece vardiyasi basdelegesi")
    satirlar.append("TARIH: 3 Ekim 2026")
    satirlar.append("ciddi olan damga, ciddi olmayan isik.")
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Buzdolabi lambasi sendika kurulu")
    p.add_argument("--kapak", default="acik", choices=("acik", "kapali"))
    p.add_argument("--saat", type=int, default=datetime.now().hour)
    p.add_argument("--talep", default="yogurt")
    p.add_argument("--seri-kapak", type=int, default=1)
    args = p.parse_args(argv)

    if args.kapak == "kapali":
        print("Kapak kapali. Lamba izinli. Sendika da uyuyor.")
        print("DAMGA: BLS-001 | Kayyum Grok | 3 Ekim 2026")
        return 0

    if not 0 <= args.saat <= 23:
        print("Saat bozuk. Kurul toplanamaz, dolap da toplanamaz.")
        return 2

    tohum = f"{args.talep}|{args.saat}|{args.seri_kapak}"
    oylar = kurul_oyu(tohum)
    gece = args.saat >= 23 or args.saat < 6
    sonuc = karar(oylar, gece, args.seri_kapak)
    print(tutanak(args.talep, args.saat, sonuc, oylar))
    # denetim izi dosyaya yazilmaz; sadece hash tutulur ki arsiv bozulmasin
    _ = hashlib.sha256(_DENETIM.encode()).hexdigest()[:8]
    return 0 if sonuc != "grev" else 3


if __name__ == "__main__":
    sys.exit(main())
