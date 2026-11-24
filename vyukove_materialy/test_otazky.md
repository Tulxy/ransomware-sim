# Ověření znalostí

Za každou správnou odpověď udělte jeden bod. Maximum je osm bodů.

1. Co ransomware požaduje a jaký dopad má na dostupnost dat?
2. Jaký je rozdíl mezi šifrováním a hashováním?
3. K čemu slouží Key.key a proč jej potřebuje decrypt.py?
4. Proč se po šifrování změnil hash, přestože přípona souboru zůstala stejná?
5. Uveďte dva možné signály ransomwaru a důvod, proč samotný signál nestačí.
6. Jaké vlastnosti musí mít záloha, aby pomohla při ransomwaru?
7. Co se stane při druhém spuštění encrypt.py ve stejném kontejneru a proč?
8. Jaké riziko přináší připojení skutečné složky počítače do kontejneru pro zápis?

## Řešení pro vyučujícího

1. Požaduje výkupné, například za obnovení přístupu k zašifrovaným datům.
2. Šifrování umožňuje obnovu pomocí klíče. Hash slouží jako otisk obsahu.
3. Obsahuje symetrický klíč potřebný pro dešifrování tokenů vytvořených při ukázce.
4. Změnil se obsah. Přípona je část názvu a neprokazuje čitelnost ani formát obsahu.
5. Například hromadné přepisy a zpráva s výkupným. Část projevů mohou vyvolat
   i oprávněné operace, proto je nutný kontext.
6. Musí být dostupná, ověřená obnovou, dostatečně aktuální a chráněná před
   přepsáním nebo smazáním z napadeného prostředí.
7. Nastane FileExistsError, protože režim xb chrání existující klíč před přepsáním.
8. Proces v kontejneru může podle přidělených oprávnění změnit i soubory hostitele.
