# OSZ Stellenüberwachung mit GitHub Actions - Setup Guide

## 📋 Was Sie bekommen

✅ **Automatisches wöchentliches Monitoring** aller OSZ-Websites  
✅ **E-Mail-Benachrichtigungen** bei neuen Stellen  
✅ **Excel-Reports** mit Änderungshistorie  
✅ **Komplett kostenlos** (GitHub Actions Free Tier)  
✅ **Wartungsfrei** - läuft automatisch  

## 🛠️ Setup-Schritte (15 Minuten)

### Schritt 1: GitHub Repository erstellen
1. Gehen Sie zu [github.com](https://github.com) und loggen Sie sich ein
2. Klicken Sie auf "New Repository"
3. Name: `osz-stellenmonitor`
4. Setzen Sie auf "Public" (für kostenloses Actions)
5. Klicken Sie "Create repository"

### Schritt 2: Repository-Geheimnisse einrichten
1. Gehen Sie zu Ihrem Repository
2. Klicken Sie auf "Settings" → "Secrets and variables" → "Actions"
3. Fügen Sie folgende Secrets hinzu:

**EMAIL_HOST**: `smtp.gmail.com` (oder Ihr E-Mail-Provider)  
**EMAIL_PORT**: `587`  
**EMAIL_USER**: `ihre-email@gmail.com`  
**EMAIL_PASS**: `ihr-app-passwort` (nicht Ihr normales Passwort!)  
**NOTIFY_EMAIL**: `empfaenger@email.com` (wohin Benachrichtigungen sollen)

### Schritt 3: Dateien hochladen
Laden Sie alle erstellten Dateien in Ihr GitHub Repository hoch:
- `.github/workflows/osz-monitor.yml`
- `scripts/osz_monitor.py`
- `scripts/requirements.txt`
- `data/previous_jobs.json` (leer: `{}`)

### Schritt 4: Erste Ausführung testen
1. Gehen Sie zu "Actions" in Ihrem Repository
2. Klicken Sie auf "OSZ Stellenmonitor"
3. Klicken Sie "Run workflow" → "Run workflow"
4. Warten Sie ~3 Minuten auf Ergebnis

## 📧 E-Mail Setup (Gmail Beispiel)

### Gmail App-Passwort erstellen:
1. Google-Konto → Sicherheit
2. 2-Faktor-Authentifizierung aktivieren
3. App-Passwörter → "Mail" auswählen
4. Generiertes Passwort als EMAIL_PASS verwenden

### Andere E-Mail-Provider:
- **Outlook**: smtp-mail.outlook.com:587
- **Yahoo**: smtp.mail.yahoo.com:587
- **GMX**: mail.gmx.net:587

## ⏰ Zeitplan

**Standard**: Jeden Montag um 8:00 Uhr (UTC)  
**Anpassbar** in der Workflow-Datei:
```yaml
schedule:
  - cron: '0 8 * * 1'  # Montag 8:00 UTC
  - cron: '0 8 * * 4'  # + Donnerstag 8:00 UTC
```

## 🔧 Anpassungen

### Mehr OSZ hinzufügen:
Bearbeiten Sie `scripts/osz_monitor.py` und fügen Sie URLs hinzu:
```python
OSZ_URLS = {
    'Neues OSZ': 'https://neues-osz.de/stellenangebote',
    # ... weitere URLs
}
```

### Benachrichtigungs-Frequenz ändern:
```yaml
# Täglich um 9:00
- cron: '0 9 * * *'
# Nur werktags um 8:00  
- cron: '0 8 * * 1-5'
```

## 📊 Monitoring & Logs

- **Ausführungshistorie**: Repository → Actions
- **Logs einsehen**: Klick auf einzelne Workflow-Runs
- **Fehlerbenachrichtigung**: GitHub sendet E-Mail bei Fehlern
- **Daten-Download**: Artifacts nach jeder Ausführung

## 🆘 Troubleshooting

**E-Mail kommt nicht an?**
- Spam-Ordner prüfen
- App-Passwort korrekt?
- SMTP-Einstellungen prüfen

**Workflow läuft nicht?**
- Repository muss "Public" sein (für kostenloses Actions)
- Secrets korrekt eingetragen?
- YAML-Syntax prüfen

**Zu viele/wenige Benachrichtigungen?**
- Schwellenwerte in `osz_monitor.py` anpassen
- Zeitplan in Workflow ändern

## 💡 Erweiterte Features

Nach dem Setup können Sie hinzufügen:
- **Slack/Teams Integration** statt E-Mail
- **Telegram Bot** für mobile Benachrichtigungen  
- **Dashboard** mit GitHub Pages
- **Keyword-Filter** für spezifische Stellen
- **Bewerbungsfristen-Reminder**

## 🎯 Nächste Schritte

1. ✅ Repository erstellen
2. ✅ Secrets konfigurieren  
3. ✅ Dateien hochladen
4. ✅ Test-Run durchführen
5. ✅ Erste E-Mail-Benachrichtigung erhalten!

**Geschätzte Einrichtungszeit**: 15 Minuten  
**Laufende Kosten**: 0€  
**Wartungsaufwand**: 0 Minuten/Monat