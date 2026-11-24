# Simulace v Dockeru

Image obsahuje Python, knihovnu cryptography, oba skripty a kopie souborů ze
složky testovaci_data. Kontejner běží pod uživatelem simulator.

Sestavení image z kořene projektu:

```sh
docker build -t ransomware-sim .
```

Spuštění interaktivního kontejneru:

```sh
docker run --rm -it --network none --cap-drop ALL --security-opt no-new-privileges ransomware-sim
```

Uvnitř kontejneru spusť postupně:

```sh
python simulace/encrypt.py
python simulace/decrypt.py
exit
```

Skripty přepisují obsah kopií souborů v /lab/testovaci_data. Klíč vznikne
v /lab/simulace/Key.key. Existující klíč zabrání dalšímu spuštění šifrování.
Pro další pokus spusť nový kontejner stejným příkazem docker run.

Při ukončení se kontejner včetně klíče a pracovních dat odstraní díky --rm.
Příkaz používá data z image a síť kontejneru je vypnutá. Soubor poznamky.txt
obsahuje fiktivní čitelný text. Ostatní testovací soubory jsou prázdné zástupné
soubory s příponami kancelářských dokumentů a fotografie.

## Zpráva s požadavkem na výkupné

Soubor `simulace/ransom_note.html` otevři v prohlížeči. Zobrazuje fiktivní
požadavek na 5 000 Kč a postup obnovy v simulaci. Stránka je statická,
stav souborů neověřuje a funguje i bez připojení k internetu.
Po novém sestavení image je také uvnitř kontejneru na
`/lab/simulace/ransom_note.html`.

## Požadavky a bezpečnost experimentu

Je potřeba běžící Docker Desktop nebo Docker Engine s podporou Linux
kontejnerů, terminál a prohlížeč pro HTML zprávu. První sestavení vyžaduje
internet pro stažení Python image a závislostí. Python na hostiteli není nutný.
Spouštějte pouze připravenou ukázku s fiktivními daty ve vlastním prostředí.
Použijte uvedený příkaz docker run, který má vypnutou síť, omezená oprávnění
a pracuje s kopiemi dat v image. Skutečná data a přihlašovací údaje do ukázky
nevkládejte. Připojení hostitelských složek pro zápis by zpřístupnilo jejich
obsah skriptům. Soubory Key.key se do image nekopírují.

## Postup pro studenty

1. Sestavte image a spusťte kontejner příkazy výše.
2. Uvnitř kontejneru zobrazte původní text a uložte jeho otisky.

   ```sh
   cat testovaci_data/poznamky.txt
   ls -l testovaci_data
   sha256sum testovaci_data/* > /tmp/puvodni.sha256
   ```

3. Spusťte šifrování a pozorujte výpis jednotlivých kroků.

   ```sh
   python simulace/encrypt.py
   cat testovaci_data/poznamky.txt
   ls -l testovaci_data
   sha256sum -c /tmp/puvodni.sha256
   ```

   Kontrola ohlásí změněné soubory jako FAILED. To je v tomto kroku očekávané.
   Text je nyní šifrovaný token. Na hostiteli otevřete ransom_note.html
   v prohlížeči a vysvětlete požadavek na výkupné.

4. Ve stejném kontejneru obnovte data a ověřte shodu.

   ```sh
   python simulace/decrypt.py
   sha256sum -c /tmp/puvodni.sha256
   cat testovaci_data/poznamky.txt
   ```

   Všechny soubory musí mít výsledek OK a text musí být znovu čitelný.
5. Pro alternativní ukázku obnovy zašifrujte data v novém kontejneru, ukončete
   jej a spusťte další ze stejného image. Původní text bude opět dostupný.
6. Odpovězte na otázky ve vyukove_materialy/test_otazky.md.

## Pokyny pro vyučujícího

Před hodinou ověřte sestavení a celý postup na školním zařízení.
Seznamte studenty s pravidly zadání a dohlédněte na použití testovacího prostředí.
Při obhajobě si nechte vysvětlit výběr souborů, práci s klíčem, změny obsahu,
ověření obnovy a rozdíl mezi dešifrováním a obnovou ze zálohy.

Rozvržení čtyř vyučovacích hodin po 45 minutách může být následující.

| Hodina | Práce a výstup |
| --- | --- |
| 1 | Princip, pravidla, rozdělení rolí, sestavení a spuštění kontejneru |
| 2 | Čtení kódu, šifrování, pozorování změn a HTML zpráva |
| 3 | Obnova, kontrola hashů, detekce a návrh obrany |
| 4 | Dokončení materiálů, test, demonstrace a obhajoba |

Skupina má podle zadání 3–5 členů. Rozdělte si implementaci a Docker,
ověření demonstrace, materiály k obraně a přípravu prezentace. U tří členů
role spojte, u pěti oddělte dokumentaci a prezentaci. Skutečná jména a přínos
doplňte podle odvedené práce. Každý člen vysvětlí princip i svou část řešení.

## Materiály a pokrytí zadání

| Kritérium | Podklad a ověření |
| --- | --- |
| Funkčnost | Šifrování, dešifrování a kontrola SHA-256 |
| Replikovatelnost | Dockerfile a postup spuštění nového kontejneru |
| Transparentnost | Zdrojové skripty, výpis kroků, porovnání obsahu |
| Dokumentace | Tento postup pro studenty a učitele |
| Výukové materiály | [Princip útoku](vyukove_materialy/princip_utoku.md) |
| Ověření znalostí | [Osm otázek a řešení](vyukove_materialy/test_otazky.md) |
| Obrana | [Detekce a obrana](vyukove_materialy/obrana_a_detekce.md), obnova z čisté kopie |

## Řešení potíží

- Chyba připojení k Docker daemonu znamená, že je třeba ověřit spuštění Dockeru.
- FileExistsError u Key.key znamená opakované šifrování. Pro nový pokus spusťte
  nový kontejner, který má původní data a čerstvý stav klíče.
- InvalidToken může znamenat chybný klíč, poškozená data nebo opakované
  dešifrování. Experiment zopakujte v novém kontejneru.
- Změny místních souborů se do existujícího image promítnou po novém sestavení.

Verze závislostí a základní image nejsou pevně uzamčené, proto další sestavení
může stáhnout novější verze. Úspěch ukázky ověřte kontrolou hashů před výukou.
