# Princip a průběh ransomwaru

Ransomware omezuje přístup k datům a požaduje výkupné. Tato pomůcka ukazuje
šifrování a následné obnovení připravených souborů. Je určena pro předmět
Kybernetická bezpečnost ve 3. ročníku oboru IT.

## Co studenti sledují

1. Učitel připraví image obsahující kopie fiktivních dat.
2. Student ručně spustí encrypt.py v kontejneru.
3. Skript vybere běžné soubory přímo v testovaci_data a přeskočí symbolické odkazy.
4. Fernet vygeneruje symetrický klíč. Stejný klíč umožní šifrování i dešifrování.
5. Klíč se uloží do simulace/Key.key a obsah každého souboru se přepíše
   šifrovaným tokenem. Názvy a přípony souborů zůstávají zachované.
6. HTML stránka představí fiktivní požadavek na výkupné.
7. decrypt.py načte uložený klíč a obnoví původní obsah.

Fernet poskytuje také kontrolu integrity. Nesprávný klíč nebo poškozený token
může způsobit chybu InvalidToken. Hash SHA-256 v demonstraci slouží k porovnání
obsahu před šifrováním a po obnově. Hashování samo o sobě data nešifruje.

## Rizika a rozsah modelu

Reálný incident může způsobit výpadek provozu, ztrátu dat a náklady na obnovu.
Útočníci mohou také data odcizit a hrozit jejich zveřejněním. Zaplacení výkupného
nezaručuje obnovení dat. Základní definici a rizika popisuje
[FBI](https://www.fbi.gov/how-we-can-help-you/common-frauds-and-scams/ransomware).

Zde spuštění představuje okamžik, kdy už útočník získal možnost spouštět kód.
Vstup přes phishing nebo zranitelnost studenti vysvětlují slovně. Síť je při
doporučeném spuštění vypnutá, klíč je pro výuku dostupný a HTML stránka je
statická. Změny se týkají kopií dat v kontejneru. Docker používá izolaci
procesů a souborového systému a vyžaduje správnou konfiguraci.

## Omezení skriptů

Skripty přepisují soubory postupně. Přerušení může zanechat směs původních
a zašifrovaných dat. Dešifrování pak může skončit na prvním neplatném souboru.
Pro opakování výuky vytvořte nový kontejner. Klíč zůstává po obnově uložený,
proto další šifrování ve stejném kontejneru skončí chybou FileExistsError.
