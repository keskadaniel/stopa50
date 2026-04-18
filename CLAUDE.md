# stopA50 — wytyczne dla Claude

## Co to jest
Jednostronicowy landing page protestu "STOP A50" (pikieta w Warszawie).
Cała treść siedzi w `index.html` — jeden plik, Tailwind CDN, inline SVG mapy.
Tekst po polsku, używamy HTML entities (`&#281;`, `&oacute;`, `&#380;`, `&mdash;` itd.) — nie surowych znaków diakrytycznych.

## Flow publikacji
1. Edytuj `index.html` lokalnie.
2. `git commit` + `git push origin main`.
3. GitHub Actions (`.github/workflows/deploy.yml`) wrzuca `index.html` do S3:
   - bucket: `s3://stopa50-web/index.html`
   - region: `eu-central-1`
   - cache: `public, max-age=300` (5 min — propagacja do tego bierze)
4. Tylko `index.html` jest deployowany. Zmiany w innych plikach (np. SVG, PDF, `generate_map.py`) NIE idą na produkcję.
5. CI potrafi trochę potrwać — to normalne.

## Zasady edycji
- Zachowuj HTML entities dla polskich znaków (reszta pliku tak robi — bądź spójny).
- Nie dodawaj nowych zależności / frameworków — strona ma zostać jednoplikowa.
- Nie commituj PDF-ów, `img.png`, `stopa50new*.txt` — to materiały robocze (PDF wykluczone przez `.gitignore`; reszta nie powinna lądować w commitach).
- Formularz zapisów idzie do Google Sheets przez Apps Script (URL w `index.html`). Jak trzeba zmienić endpoint — zmienia się w HTML.
- Google Analytics: `G-MN0VKXQ52Y` (już wpięty).
- Kontakt: `kontakt@a50.pl`.

## Commity
- Po polsku, krótko, rzeczowo (patrz `git log`).
- Commituj tylko realnie zmienione pliki (`git add <plik>`, nie `-A`).
- Push na `main` = deploy. Przed pushem zweryfikuj zmiany.

## Infrastruktura AWS / hosting
- **AWS account:** `402275401857` (region `eu-central-1`).
- **S3 bucket:** `stopa50-web` — static website hosting włączony (`index.html` jako IndexDocument), bucket policy `PublicRead` na `s3:GetObject`. Endpoint: `stopa50-web.s3-website.eu-central-1.amazonaws.com`.
- **CloudFront:** dystrybucja `E2RBG6WPIS20JP` (`df8cbbbqabhy3.cloudfront.net`).
  - Aliasy: `a50.pl`, `www.a50.pl`.
  - Origin: website endpoint S3.
  - Viewer protocol: `redirect-to-https`.
  - Cache: DefaultTTL 300, MinTTL 0, MaxTTL 86400. Price class: `PriceClass_100` (EU/US).
- **DNS:** Route53 NIE jest używany — domena `a50.pl` prowadzona u zewnętrznego rejestratora, CNAME/ALIAS kieruje na CloudFront.
- **Lokalne CLI:** `aws` ma dostęp (root account) — można czytać stan (`aws s3 ls s3://stopa50-web/`, `aws cloudfront get-distribution ...`). Nie używaj roota do modyfikacji bez potrzeby.

## Propagacja zmian po pushu
- GitHub Actions uploaduje `index.html` do S3 z `Cache-Control: max-age=300`.
- CloudFront DefaultTTL = 300, więc do ~5 min użytkownicy widzą starą wersję.
- Jeśli zmiana musi pójść NATYCHMIAST: `aws cloudfront create-invalidation --distribution-id E2RBG6WPIS20JP --paths "/index.html"` (pierwsze 1000 inwalidacji/mies. darmowe). Zwykle nie trzeba — 5 min cache to akceptowalne.

## Czego NIE ruszać bez pytania
- `.github/workflows/deploy.yml` — zmiana psuje deploy.
- Sekrety AWS (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) — żyją w GitHub Secrets.
- Bucket policy / CloudFront config — zmiana może zdjąć stronę z netu.
- Struktura HTML sekcji mapy (inline SVG, linie 527+) — duża, łatwo uszkodzić.
