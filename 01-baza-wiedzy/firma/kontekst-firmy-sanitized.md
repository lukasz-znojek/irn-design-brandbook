# Kontekst firmy IRIN — wersja sanitized

> Wersja bezpieczna do publicznego repozytorium, opracowana z wewnętrznego materiału źródłowego. Uzupełnia `kontekst-firmy.md` o mechanikę finansową i compliance rozliczeń dofinansowania, której tamta karta (linie biznesowe, struktura) nie opisuje — nie zastępuje jej.

## Kto jest dostawcą

Nazwa prawna: **Instytut Rozwoju i Nauki sp. z o.o.**, marka IRIN.

Dane rejestrowe (jawne w Krajowym Rejestrze Sądowym): KRS 0001032499 · NIP 9592061542 · REGON 525113640 · ul. Karola Olszewskiego 6, 25-663 Kielce.

Dwie pozycje wymagane przez art. 206 KSH na pismach i zamówieniach handlowych, **odczytane 2026-09-03 z odpisu pełnego w rejestrze KRS** (`api-krs.ms.gov.pl/api/krs/OdpisPelny/0001032499?rejestr=P`, stan z dnia 15.07.2026):

- **sąd rejestrowy:** Sąd Rejonowy w Kielcach, X Wydział Gospodarczy Krajowego Rejestru Sądowego
- **kapitał zakładowy:** 40 000,00 zł

Kapitał zakładowy zmienia się uchwałą i wpisem do rejestru, więc przed każdym dokumentem powołującym się na tę kwotę sprawdza się datę „stan z dnia" w świeżym odpisie, nie datę tego pliku. To jedyne dwie wartości w tej karcie, których founder nie potwierdził osobiście - pochodzą wprost z rejestru.

Te dane trafiają do stopki dokumentu wydawanego uczestnikowi szkolenia i do danych dostawcy w karcie usługi — bo tego wymaga jednoznaczna identyfikacja realizatora na dokumencie formalnym (patrz `../prawo/kfs.md`, `../prawo/bur.md`). Numer wpisu do rejestru podmiotów świadczących usługi rozwojowe (BUR) nie jest tu podawany — każdy dokument, który go wymaga, powinien odczytać go z aktualnego profilu dostawcy w BUR, nie wpisywać z pamięci ani z tego pliku.

**Zasada minimalizacji:** ten plik publikuje wyłącznie dane jawne (KRS) i niezbędne do formalnej identyfikacji dostawcy na dokumencie. Dane kontaktowe o charakterze operacyjnym (adres e-mail, numer telefonu, adres strony) nie są tu powielane — nie są potrzebne do identyfikacji dostawcy na dokumencie formalnym, a ich miejsce jest w materiałach, których to dotyczy (np. papier firmowy, wizytówka), nie w karcie kontekstu firmy.

## Trzy linie biznesowe

IRIN działa w trzech obszarach: aplikacje dla przedstawicieli handlowych, usługi pozyskiwania pożyczek i dofinansowań, oraz dofinansowane szkolenia zawodowe wydające zaświadczenia KFS i certyfikaty BUR. Planowany jest też portal sprzedaży szkoleń online.

Konsekwencja dla treści dokumentów: klient linii szkoleniowej jest jednocześnie potencjalnym klientem linii dofinansowaniowej i odwrotnie. Materiał o charakterze prezentacyjnym (np. oferta, prezentacja produktowa) może to odzwierciedlać; dokument o charakterze formalnym wobec instytucji (np. karta usługi BUR) — nie powinien nieść treści z innej linii biznesowej, bo to nie jego funkcja.

## Stawka VAT — zasada, nie liczba

Klasyfikacja podatkowa (zwolnienie z VAT albo stawka 23%) zależy od konkretnej usługi i wymaga potwierdzenia księgowego przed publikacją każdej nowej kategorii usługi. Zdanie w rodzaju „u nas zwykle jest zwolnione" nie jest podstawą prawną i nie powinno pojawiać się w żadnym dokumencie zewnętrznym — podstawę zwolnienia albo zastosowanie stawki wskazuje się jawnie, z potwierdzeniem księgowości.

## Modele rozliczenia dofinansowania — cztery wzorce

Konkretne szkolenie dofinansowane działa według jednego z czterech ogólnych wzorców rozliczenia. Model wybiera instytucja finansująca (operator/urząd), nie IRIN — ale model przesądza, co wolno obiecać w ofercie.

| Model | Mechanizm | Skutek dla oferty |
|---|---|---|
| **Dopłata instytucji do dostawcy usługi** | uczestnik/pracodawca wpłaca udział własny przed usługą, instytucja dopłaca resztę po usłudze | uczestnik wykłada tylko swoją część — najmocniejszy argument sprzedażowy |
| **Refundacja uczestnikowi** | uczestnik/pracodawca płaci dostawcy 100% ceny, sam odbiera zwrot od instytucji po usłudze | uczestnik finansuje całość i czeka na zwrot — realny koszt finansowy po jego stronie, warty adresowania w ofercie |
| **Program lojalnościowy / bonowy** | rozliczenie wewnętrzne dostawcy usługi | dotyczy **wyłącznie usług komercyjnych**, nigdy dofinansowanych |
| **Komercyjny** | uczestnik/pracodawca płaci w całości | bez limitów instytucji, cena ustalana swobodnie |

## Granica compliance, której nie wolno przekroczyć

**Wkład własny w usłudze dofinansowanej musi być realnie poniesiony.** Nie wolno go zwracać ani refinansować uczestnikowi żadnym kanałem, w tym poprzez rabat, program lojalnościowy czy zniżkę na kolejną usługę — to nieprawidłowość wobec zasad BUR i EFS, a nie kwestia księgowania. Zmiana nazwy mechanizmu ani przeniesienie go do innego podmiotu tego nie sanuje: liczy się treść ekonomiczna operacji, nie jej nazwa.

Skutek dla każdej treści wychodzącej na zewnątrz: **żaden materiał (oferta, prezentacja, karta usługi) nie może sugerować zwrotu, rabatu ani rekompensaty wkładu własnego przy usłudze dofinansowanej.** Rabat na cenę usługi dofinansowanej jest osobnym zagadnieniem — obniża podstawę dofinansowania i wymaga zgody instytucji finansującej, nie jest decyzją handlową dostawcy.

## Numer naboru

Nabór ma numer nadany przez instytucję finansującą. Dostawca usługi nie tworzy własnej numeracji naborów ani nie miesza jej z identyfikatorem programu szkoleniowego — to dwie różne rzeczy.

## Warstwa wizualna

Ten plik nie dotyka warstwy wizualnej. Kolory, krój pisma, znak i wzory dokumentów pochodzą wyłącznie z `03-pakiet-claude-design/` i z bieżącego brandbooku IRIN — nie z tego pliku i nie z żadnej starszej wersji identyfikacji.

## Notatka o sanitizacji

Źródło: wewnętrzny materiał kontekstowy IRIN, przetworzony 2026-09-02.

Usunięto lub uogólniono:
- **dane osobowe / kadrowe** — role przypisania trenerów, odwołania do „kartoteki osób" i sposobu ich prowadzenia w wewnętrznym systemie,
- **wewnętrzne procedury operacyjne/sprzedażowe** — sekcję o przekazaniu zadań między rolami wewnętrznymi (zespół obsługowy, kierownik zespołu, opiekun projektu) i o adresacie „karty rozliczenia projektu” usunięto w całości; nie wnosiła nic do treści publicznej,
- **metodykę kosztową i prowizyjną** — usunięto opis progu rentowności, tytułów prowizyjnych (partner / zespół obsługowy / pozyskanie) i klucza narzutu kosztów wspólnych; są to dane operacyjne firmy, nieprzydatne do dokumentu publicznego i potencjalnie ujawniające sposób kalkulacji marży,
- **identyfikatory systemowe** — odwołania do konkretnych plików wewnętrznego systemu/skilla (ścieżki takie jak `wymogi-bur.md`, `../assets/`), którego nie ma w tym repozytorium,
- **nazwę własną mechanizmu lojalnościowego** — zastąpiono opisem ogólnym („program lojalnościowy / bonowy”), bez nazwy handlowej.

Zastosowano dodatkowo zasadę minimalizacji (2026-09-02): usunięto adres e-mail, numer telefonu i adres strony biura — to dane kontaktowe o charakterze operacyjnym, niepotrzebne do jednoznacznej identyfikacji dostawcy na dokumencie formalnym (jedynej funkcji, jaką ten plik przypisuje danym rejestrowym). Pozostawiono wyłącznie KRS, NIP, REGON i adres siedziby: są to dane jawne w Krajowym Rejestrze Sądowym i niezbędne do identyfikacji realizatora, którą wprost wymagają `../prawo/kfs.md` i `../prawo/bur.md`. Ich obecność w publicznym repozytorium nie stanowi ujawnienia tajemnicy handlowej. **Potwierdzone przez foundera 2026-09-02:** dane są poprawne i zostają w publicznym repozytorium; ta sama forma prawna i siedziba obowiązują w `kontekst-firmy.md` i w `/02-szablony-dokumentow/papier-firmowy.md`.
