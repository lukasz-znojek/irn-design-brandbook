# Pomiar kontrastu WCAG 2.1 - warianty palety v2

Plik generowany skryptem `../narzedzia/generuj-podglad-i-kontrast.py` z `../tokens/palette-options-v2.json`. Kontrast liczony wzorem na luminancję względną sRGB (WCAG 2.1), nie przepisany z żadnego źródła. Progi: AA tekst normalny 4,5:1, AA duży tekst 3:1, AAA 7:1, elementy nietekstowe 3:1. Znak ⚠ oznacza wynik poniżej progu wymaganego dla danej pary.

## Wariant 1 - Kaszmir Aksamit (obecna, uporządkowana)

| Para | Kolory | Kontrast | Ocena WCAG 2.1 |
|---|---|---|---|
| Tekst korpusu (text-primary) na tle strony (background) | `#1E1611` na `#F7F3EA` | 16,10:1 | AAA |
| Tekst korpusu (text-primary) na karcie (surface) | `#1E1611` na `#F2ECE1` | 15,16:1 | AAA |
| Tekst pomocniczy (text-secondary) na tle strony | `#5B4837` na `#F7F3EA` | 7,81:1 | AAA |
| Tekst pomocniczy (text-secondary) na karcie (surface) | `#5B4837` na `#F2ECE1` | 7,36:1 | AAA |
| Link (link) na tle strony | `#AC151F` na `#F7F3EA` | 6,58:1 | AA |
| Link (link) na karcie (surface) | `#AC151F` na `#F2ECE1` | 6,20:1 | AA |
| Nagłówek H1 (primary) na karcie - duży tekst | `#4A1D26` na `#F2ECE1` | 11,95:1 | AAA |
| Nagłówek H2 (secondary) na karcie - duży tekst | `#1B2B26` na `#F2ECE1` | 12,58:1 | AAA |
| Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy | `#8C5026` na `#F2ECE1` | 5,43:1 | AA |
| CTA podstawowe: tekst w kolorze background na primary | `#F7F3EA` na `#4A1D26` | 12,69:1 | AAA |
| CTA akcentowe: tekst #F7F3EA na accent | `#F7F3EA` na `#8C5026` | 5,76:1 | AA |
| Info jako tekst na karcie | `#2E4F4A` na `#F2ECE1` | 7,65:1 | AAA |
| Success jako tekst na karcie | `#2F4A32` na `#F2ECE1` | 8,32:1 | AAA |
| Warning jako tekst na karcie | `#D9AC4A` na `#F2ECE1` | 1,80:1 | poniżej AA ⚠ |
| Etykieta warning: tekst #1E1611 na warning | `#1E1611` na `#D9AC4A` | 8,45:1 | AAA |
| Error jako tekst na karcie | `#AC151F` na `#F2ECE1` | 6,20:1 | AA |
| Etykieta success: tekst background na success | `#F7F3EA` na `#2F4A32` | 8,83:1 | AAA |
| Etykieta error: tekst background na error | `#F7F3EA` na `#AC151F` | 6,58:1 | AA |
| Etykieta info: tekst background na info | `#F7F3EA` na `#2E4F4A` | 8,13:1 | AAA |
| Pas tytułowy: neutral-light na neutral-dark | `#E4DACB` na `#1E1611` | 12,89:1 | AAA |
| Linia (border) na tle strony - element nietekstowy | `#C3BDB3` na `#F7F3EA` | 1,69:1 | poniżej AA ⚠ |
| Rozróżnialność: link względem text-primary | `#AC151F` na `#1E1611` | 2,45:1 | informacyjnie |
| Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień) | `#4A1D26` na `#AC151F` | 1,93:1 | informacyjnie |

**Poniżej progu:** Warning jako tekst na karcie (1,80:1); Linia (border) na tle strony - element nietekstowy (1,69:1).

## Wariant 2 - Atrament i Papier (granat instytucjonalny na ciepłym papierze)

| Para | Kolory | Kontrast | Ocena WCAG 2.1 |
|---|---|---|---|
| Tekst korpusu (text-primary) na tle strony (background) | `#141A26` na `#F8F5EE` | 16,00:1 | AAA |
| Tekst korpusu (text-primary) na karcie (surface) | `#141A26` na `#F2EEE4` | 15,04:1 | AAA |
| Tekst pomocniczy (text-secondary) na tle strony | `#56544F` na `#F8F5EE` | 6,95:1 | AA |
| Tekst pomocniczy (text-secondary) na karcie (surface) | `#56544F` na `#F2EEE4` | 6,53:1 | AA |
| Link (link) na tle strony | `#1F5AA6` na `#F8F5EE` | 6,28:1 | AA |
| Link (link) na karcie (surface) | `#1F5AA6` na `#F2EEE4` | 5,90:1 | AA |
| Nagłówek H1 (primary) na karcie - duży tekst | `#1F2D4F` na `#F2EEE4` | 11,72:1 | AAA |
| Nagłówek H2 (secondary) na karcie - duży tekst | `#7A5A36` na `#F2EEE4` | 5,42:1 | AA |
| Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy | `#875512` na `#F2EEE4` | 5,43:1 | AA |
| CTA podstawowe: tekst w kolorze background na primary | `#F8F5EE` na `#1F2D4F` | 12,47:1 | AAA |
| CTA akcentowe: tekst #F8F5EE na accent | `#F8F5EE` na `#875512` | 5,78:1 | AA |
| Info jako tekst na karcie | `#2B5F8E` na `#F2EEE4` | 5,79:1 | AA |
| Success jako tekst na karcie | `#2E6B4F` na `#F2EEE4` | 5,44:1 | AA |
| Warning jako tekst na karcie | `#C98F1B` na `#F2EEE4` | 2,44:1 | poniżej AA ⚠ |
| Etykieta warning: tekst #141A26 na warning | `#141A26` na `#C98F1B` | 6,16:1 | AA |
| Error jako tekst na karcie | `#B0322E` na `#F2EEE4` | 5,42:1 | AA |
| Etykieta success: tekst background na success | `#F8F5EE` na `#2E6B4F` | 5,79:1 | AA |
| Etykieta error: tekst background na error | `#F8F5EE` na `#B0322E` | 5,77:1 | AA |
| Etykieta info: tekst background na info | `#F8F5EE` na `#2B5F8E` | 6,16:1 | AA |
| Pas tytułowy: neutral-light na neutral-dark | `#E5E0D5` na `#141A26` | 13,24:1 | AAA |
| Linia (border) na tle strony - element nietekstowy | `#C9C2B4` na `#F8F5EE` | 1,63:1 | poniżej AA ⚠ |
| Rozróżnialność: link względem text-primary | `#1F5AA6` na `#141A26` | 2,55:1 | informacyjnie |
| Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień) | `#1F2D4F` na `#B0322E` | 2,16:1 | informacyjnie |

**Poniżej progu:** Warning jako tekst na karcie (2,44:1); Linia (border) na tle strony - element nietekstowy (1,63:1).

## Wariant 3 - Zieleń Instytutu (leśna zieleń i mosiądz)

| Para | Kolory | Kontrast | Ocena WCAG 2.1 |
|---|---|---|---|
| Tekst korpusu (text-primary) na tle strony (background) | `#16201A` na `#F6F5EF` | 15,31:1 | AAA |
| Tekst korpusu (text-primary) na karcie (surface) | `#16201A` na `#EFEFE6` | 14,46:1 | AAA |
| Tekst pomocniczy (text-secondary) na tle strony | `#4F5A52` na `#F6F5EF` | 6,59:1 | AA |
| Tekst pomocniczy (text-secondary) na karcie (surface) | `#4F5A52` na `#EFEFE6` | 6,23:1 | AA |
| Link (link) na tle strony | `#8A5814` na `#F6F5EF` | 5,51:1 | AA |
| Link (link) na karcie (surface) | `#8A5814` na `#EFEFE6` | 5,21:1 | AA |
| Nagłówek H1 (primary) na karcie - duży tekst | `#1F3D2E` na `#EFEFE6` | 10,29:1 | AAA |
| Nagłówek H2 (secondary) na karcie - duży tekst | `#5A6B54` na `#EFEFE6` | 4,95:1 | AA |
| Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy | `#8F5C16` na `#EFEFE6` | 4,89:1 | AA |
| CTA podstawowe: tekst w kolorze background na primary | `#F6F5EF` na `#1F3D2E` | 10,89:1 | AAA |
| CTA akcentowe: tekst #F6F5EF na accent | `#F6F5EF` na `#8F5C16` | 5,18:1 | AA |
| Info jako tekst na karcie | `#2C6B85` na `#EFEFE6` | 5,12:1 | AA |
| Success jako tekst na karcie | `#2F7A4E` na `#EFEFE6` | 4,52:1 | AA |
| Warning jako tekst na karcie | `#D19B2C` na `#EFEFE6` | 2,15:1 | poniżej AA ⚠ |
| Etykieta warning: tekst #16201A na warning | `#16201A` na `#D19B2C` | 6,72:1 | AA |
| Error jako tekst na karcie | `#A9302C` na `#EFEFE6` | 5,77:1 | AA |
| Etykieta success: tekst background na success | `#F6F5EF` na `#2F7A4E` | 4,79:1 | AA |
| Etykieta error: tekst background na error | `#F6F5EF` na `#A9302C` | 6,11:1 | AA |
| Etykieta info: tekst background na info | `#F6F5EF` na `#2C6B85` | 5,42:1 | AA |
| Pas tytułowy: neutral-light na neutral-dark | `#E2E5DB` na `#16201A` | 13,11:1 | AAA |
| Linia (border) na tle strony - element nietekstowy | `#C6CBBE` na `#F6F5EF` | 1,52:1 | poniżej AA ⚠ |
| Rozróżnialność: link względem text-primary | `#8A5814` na `#16201A` | 2,78:1 | informacyjnie |
| Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień) | `#1F3D2E` na `#A9302C` | 1,78:1 | informacyjnie |

**Poniżej progu:** Warning jako tekst na karcie (2,15:1); Linia (border) na tle strony - element nietekstowy (1,52:1).

## Wariant 4 - Grafit techniczny (chłodne neutrale, jeden ciepły akcent)

| Para | Kolory | Kontrast | Ocena WCAG 2.1 |
|---|---|---|---|
| Tekst korpusu (text-primary) na tle strony (background) | `#15181C` na `#F7F8FA` | 16,76:1 | AAA |
| Tekst korpusu (text-primary) na karcie (surface) | `#15181C` na `#FFFFFF` | 17,81:1 | AAA |
| Tekst pomocniczy (text-secondary) na tle strony | `#4B5563` na `#F7F8FA` | 7,11:1 | AAA |
| Tekst pomocniczy (text-secondary) na karcie (surface) | `#4B5563` na `#FFFFFF` | 7,56:1 | AAA |
| Link (link) na tle strony | `#175CD3` na `#F7F8FA` | 5,63:1 | AA |
| Link (link) na karcie (surface) | `#175CD3` na `#FFFFFF` | 5,99:1 | AA |
| Nagłówek H1 (primary) na karcie - duży tekst | `#22272E` na `#FFFFFF` | 15,02:1 | AAA |
| Nagłówek H2 (secondary) na karcie - duży tekst | `#4A5563` na `#FFFFFF` | 7,58:1 | AAA |
| Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy | `#B84A0B` na `#FFFFFF` | 5,22:1 | AA |
| CTA podstawowe: tekst w kolorze background na primary | `#F7F8FA` na `#22272E` | 14,14:1 | AAA |
| CTA akcentowe: tekst #F7F8FA na accent | `#F7F8FA` na `#B84A0B` | 4,91:1 | AA |
| Info jako tekst na karcie | `#175CD3` na `#FFFFFF` | 5,99:1 | AA |
| Success jako tekst na karcie | `#1E7B4B` na `#FFFFFF` | 5,26:1 | AA |
| Warning jako tekst na karcie | `#B7791F` na `#FFFFFF` | 3,64:1 | AA tylko duży tekst ⚠ |
| Etykieta warning: tekst #15181C na warning | `#15181C` na `#B7791F` | 4,89:1 | AA |
| Error jako tekst na karcie | `#B42318` na `#FFFFFF` | 6,57:1 | AA |
| Etykieta success: tekst background na success | `#F7F8FA` na `#1E7B4B` | 4,95:1 | AA |
| Etykieta error: tekst background na error | `#F7F8FA` na `#B42318` | 6,19:1 | AA |
| Etykieta info: tekst background na info | `#F7F8FA` na `#175CD3` | 5,63:1 | AA |
| Pas tytułowy: neutral-light na neutral-dark | `#E6E8EB` na `#15181C` | 14,51:1 | AAA |
| Linia (border) na tle strony - element nietekstowy | `#D0D5DB` na `#F7F8FA` | 1,39:1 | poniżej AA ⚠ |
| Rozróżnialność: link względem text-primary | `#175CD3` na `#15181C` | 2,97:1 | informacyjnie |
| Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień) | `#22272E` na `#B42318` | 2,29:1 | informacyjnie |

**Poniżej progu:** Warning jako tekst na karcie (3,64:1); Linia (border) na tle strony - element nietekstowy (1,39:1).

## Wariant 5 - Terakota i piasek (ciepły, ziemisty, ludzki)

| Para | Kolory | Kontrast | Ocena WCAG 2.1 |
|---|---|---|---|
| Tekst korpusu (text-primary) na tle strony (background) | `#2B1F17` na `#FAF5EC` | 14,75:1 | AAA |
| Tekst korpusu (text-primary) na karcie (surface) | `#2B1F17` na `#F4EBDC` | 13,55:1 | AAA |
| Tekst pomocniczy (text-secondary) na tle strony | `#6A5646` na `#FAF5EC` | 6,38:1 | AA |
| Tekst pomocniczy (text-secondary) na karcie (surface) | `#6A5646` na `#F4EBDC` | 5,86:1 | AA |
| Link (link) na tle strony | `#3B6D8C` na `#FAF5EC` | 5,15:1 | AA |
| Link (link) na karcie (surface) | `#3B6D8C` na `#F4EBDC` | 4,73:1 | AA |
| Nagłówek H1 (primary) na karcie - duży tekst | `#8E3B1E` na `#F4EBDC` | 6,36:1 | AA |
| Nagłówek H2 (secondary) na karcie - duży tekst | `#5C6A3B` na `#F4EBDC` | 4,96:1 | AA |
| Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy | `#914A14` na `#F4EBDC` | 5,56:1 | AA |
| CTA podstawowe: tekst w kolorze background na primary | `#FAF5EC` na `#8E3B1E` | 6,92:1 | AA |
| CTA akcentowe: tekst #FAF5EC na accent | `#FAF5EC` na `#914A14` | 6,05:1 | AA |
| Info jako tekst na karcie | `#3B6D8C` na `#F4EBDC` | 4,73:1 | AA |
| Success jako tekst na karcie | `#377033` na `#F4EBDC` | 5,04:1 | AA |
| Warning jako tekst na karcie | `#D9A441` na `#F4EBDC` | 1,90:1 | poniżej AA ⚠ |
| Etykieta warning: tekst #2B1F17 na warning | `#2B1F17` na `#D9A441` | 7,12:1 | AAA |
| Error jako tekst na karcie | `#B3261E` na `#F4EBDC` | 5,53:1 | AA |
| Etykieta success: tekst background na success | `#FAF5EC` na `#377033` | 5,48:1 | AA |
| Etykieta error: tekst background na error | `#FAF5EC` na `#B3261E` | 6,02:1 | AA |
| Etykieta info: tekst background na info | `#FAF5EC` na `#3B6D8C` | 5,15:1 | AA |
| Pas tytułowy: neutral-light na neutral-dark | `#EBDFCC` na `#2B1F17` | 12,17:1 | AAA |
| Linia (border) na tle strony - element nietekstowy | `#D6C7B0` na `#FAF5EC` | 1,53:1 | poniżej AA ⚠ |
| Rozróżnialność: link względem text-primary | `#3B6D8C` na `#2B1F17` | 2,86:1 | informacyjnie |
| Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień) | `#8E3B1E` na `#B3261E` | 1,15:1 | informacyjnie |

**Poniżej progu:** Warning jako tekst na karcie (1,90:1); Linia (border) na tle strony - element nietekstowy (1,53:1).

## Wariant 6 - Bordo akademickie (uroczyste, dyplomowe, chłodne neutrale)

| Para | Kolory | Kontrast | Ocena WCAG 2.1 |
|---|---|---|---|
| Tekst korpusu (text-primary) na tle strony (background) | `#1B1A1C` na `#FAF8F5` | 16,36:1 | AAA |
| Tekst korpusu (text-primary) na karcie (surface) | `#1B1A1C` na `#FFFFFF` | 17,34:1 | AAA |
| Tekst pomocniczy (text-secondary) na tle strony | `#57524E` na `#FAF8F5` | 7,28:1 | AAA |
| Tekst pomocniczy (text-secondary) na karcie (surface) | `#57524E` na `#FFFFFF` | 7,71:1 | AAA |
| Link (link) na tle strony | `#8A2436` na `#FAF8F5` | 8,30:1 | AAA |
| Link (link) na karcie (surface) | `#8A2436` na `#FFFFFF` | 8,80:1 | AAA |
| Nagłówek H1 (primary) na karcie - duży tekst | `#6B1E2E` na `#FFFFFF` | 11,35:1 | AAA |
| Nagłówek H2 (secondary) na karcie - duży tekst | `#2E3A47` na `#FFFFFF` | 11,59:1 | AAA |
| Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy | `#8A6A1C` na `#FFFFFF` | 5,05:1 | AA |
| CTA podstawowe: tekst w kolorze background na primary | `#FAF8F5` na `#6B1E2E` | 10,71:1 | AAA |
| CTA akcentowe: tekst #FAF8F5 na accent | `#FAF8F5` na `#8A6A1C` | 4,76:1 | AA |
| Info jako tekst na karcie | `#2F5F8A` na `#FFFFFF` | 6,72:1 | AA |
| Success jako tekst na karcie | `#2C6B46` na `#FFFFFF` | 6,37:1 | AA |
| Warning jako tekst na karcie | `#C4922C` na `#FFFFFF` | 2,80:1 | poniżej AA ⚠ |
| Etykieta warning: tekst #1B1A1C na warning | `#1B1A1C` na `#C4922C` | 6,19:1 | AA |
| Error jako tekst na karcie | `#B3261E` na `#FFFFFF` | 6,54:1 | AA |
| Etykieta success: tekst background na success | `#FAF8F5` na `#2C6B46` | 6,01:1 | AA |
| Etykieta error: tekst background na error | `#FAF8F5` na `#B3261E` | 6,17:1 | AA |
| Etykieta info: tekst background na info | `#FAF8F5` na `#2F5F8A` | 6,34:1 | AA |
| Pas tytułowy: neutral-light na neutral-dark | `#E8E4DF` na `#1B1A1C` | 13,70:1 | AAA |
| Linia (border) na tle strony - element nietekstowy | `#D5CFC7` na `#FAF8F5` | 1,46:1 | poniżej AA ⚠ |
| Rozróżnialność: link względem text-primary | `#8A2436` na `#1B1A1C` | 1,97:1 | informacyjnie |
| Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień) | `#6B1E2E` na `#B3261E` | 1,74:1 | informacyjnie |

**Poniżej progu:** Warning jako tekst na karcie (2,80:1); Linia (border) na tle strony - element nietekstowy (1,46:1).

## Wariant 7 - Sygnał (monochrom i jeden żywy akcent)

| Para | Kolory | Kontrast | Ocena WCAG 2.1 |
|---|---|---|---|
| Tekst korpusu (text-primary) na tle strony (background) | `#111111` na `#FFFFFF` | 18,88:1 | AAA |
| Tekst korpusu (text-primary) na karcie (surface) | `#111111` na `#F4F4F4` | 17,17:1 | AAA |
| Tekst pomocniczy (text-secondary) na tle strony | `#555555` na `#FFFFFF` | 7,46:1 | AAA |
| Tekst pomocniczy (text-secondary) na karcie (surface) | `#555555` na `#F4F4F4` | 6,78:1 | AA |
| Link (link) na tle strony | `#0B57D0` na `#FFFFFF` | 6,39:1 | AA |
| Link (link) na karcie (surface) | `#0B57D0` na `#F4F4F4` | 5,81:1 | AA |
| Nagłówek H1 (primary) na karcie - duży tekst | `#111111` na `#F4F4F4` | 17,17:1 | AAA |
| Nagłówek H2 (secondary) na karcie - duży tekst | `#3D3D3D` na `#F4F4F4` | 9,88:1 | AAA |
| Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy | `#B84500` na `#F4F4F4` | 4,91:1 | AA |
| CTA podstawowe: tekst w kolorze background na primary | `#FFFFFF` na `#111111` | 18,88:1 | AAA |
| CTA akcentowe: tekst #FFFFFF na accent | `#FFFFFF` na `#B84500` | 5,40:1 | AA |
| Info jako tekst na karcie | `#1B5FC1` na `#F4F4F4` | 5,53:1 | AA |
| Success jako tekst na karcie | `#1B7A3D` na `#F4F4F4` | 4,90:1 | AA |
| Warning jako tekst na karcie | `#E3A81B` na `#F4F4F4` | 1,93:1 | poniżej AA ⚠ |
| Etykieta warning: tekst #111111 na warning | `#111111` na `#E3A81B` | 8,89:1 | AAA |
| Error jako tekst na karcie | `#C1281E` na `#F4F4F4` | 5,32:1 | AA |
| Etykieta success: tekst background na success | `#FFFFFF` na `#1B7A3D` | 5,39:1 | AA |
| Etykieta error: tekst background na error | `#FFFFFF` na `#C1281E` | 5,85:1 | AA |
| Etykieta info: tekst background na info | `#FFFFFF` na `#1B5FC1` | 6,08:1 | AA |
| Pas tytułowy: neutral-light na neutral-dark | `#E6E6E6` na `#111111` | 15,13:1 | AAA |
| Linia (border) na tle strony - element nietekstowy | `#C8C8C8` na `#FFFFFF` | 1,67:1 | poniżej AA ⚠ |
| Rozróżnialność: link względem text-primary | `#0B57D0` na `#111111` | 2,96:1 | informacyjnie |
| Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień) | `#111111` na `#C1281E` | 3,23:1 | informacyjnie |

**Poniżej progu:** Warning jako tekst na karcie (1,93:1); Linia (border) na tle strony - element nietekstowy (1,67:1).
