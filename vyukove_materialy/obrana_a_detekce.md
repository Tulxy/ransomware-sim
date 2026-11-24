# Obrana a detekce

## Co pozorovat při demonstraci

Porovnejte obsah poznamky.txt, velikosti souborů a jejich SHA-256 před spuštěním
a po něm podle README. Výpis skriptu ukazuje jednotlivé přepsané soubory.
Změna hashe prokazuje změnu obsahu. Sama neurčuje, zda šlo o útok.

V praxi bezpečnostní nástroje mohou sledovat neobvyklé hromadné zápisy,
procesy měnící velké množství dokumentů a vznik zpráv s výkupným.
Je potřeba vyhodnotit souvislosti, protože podobnou aktivitu může způsobit
i legitimní program. Tento projekt obsahuje ruční pozorování změn.

## Prevence a omezení dopadu

- Udržovat operační systém a aplikace aktualizované.
- Používat vícefaktorové ověřování a omezit vzdálené přístupy.
- Přidělovat uživatelům jen potřebná oprávnění a oddělovat části sítě.
- Procvičovat rozpoznání phishingu a hlášení podezřelých příloh.
- Pravidelně vytvářet oddělené nebo offline zálohy a testovat jejich obnovu.
- Sledovat události pomocí ochrany koncových zařízení a centralizovaných logů.

Tato opatření i postup reakce rozpracovává společný průvodce
[CISA a partnerů](https://www.ic3.gov/CSA/2023/231019.pdf).

## Reakce na podezření ve škole

Student přeruší experiment a informuje učitele. U skutečného incidentu se
postupuje podle školního incidentního plánu, izolují se zasažená zařízení
od sítě a zachovají se dostupné důkazy pro správce. Obnova z ověřené zálohy
probíhá až v připraveném čistém prostředí po vyřešení příčiny kompromitace.

## Praktická obnova bez dešifrovacího klíče

Po zašifrování ukončete výukový kontejner příkazem exit. Nový kontejner ze
stejného image obsahuje původní data. Porovnejte jejich hash s výchozím stavem.
Tím předvedete obnovu z předem připravené čisté kopie. V praxi musí být záloha
dostatečně aktuální a oddělená od oprávnění napadeného systému.
