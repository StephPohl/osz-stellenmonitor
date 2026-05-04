# 🎯 OSZ Stellenmonitor - Automatische Überwachung

Kostenlose, vollautomatische Überwachung aller OSZ-Stellenausschreibungen in Berlin und Brandenburg mit GitHub Actions.

## ✨ Features

- 🤖 **Vollautomatisch**: Läuft jeden Montag um 8:00 Uhr
- 📧 **E-Mail-Benachrichtigungen**: Bei neuen Stellen sofort informiert
- 📊 **Excel-Reports**: Übersichtliche Zusammenfassung aller Stellen
- 💰 **Komplett kostenlos**: Nutzt GitHub Actions Free Tier
- 🔄 **Wartungsfrei**: Keine Updates oder Wartung nötig
- 📱 **Mobile-freundlich**: E-Mails auf allen Geräten

## 🎯 Überwachte Quellen

### Berlin
- Louise-Schroeder-Schule (OSZ Wirtschaft/Verwaltung)
- Berlin Karriereportal (Senatsverwaltung)
- OSZ IMT (Informations-/Medizintechnik)

### Brandenburg  
- OSZ I Spree-Neiße (Metalltechnik, Elektrotechnik, Informatik)
- OSZ II Spree-Neiße (Wirtschaft, Gastronomie, Verwaltung)
- MBJS Brandenburg (Zentrale Stellenausschreibungen)

## 📊 Was Sie erhalten

### Wöchentliche E-Mail mit:
- ✅ Anzahl neuer Stellen seit letzter Prüfung
- ✅ Vollständige Liste aller aktuellen OSZ-Stellen
- ✅ Direkte Links zu Stellenausschreibungen
- ✅ Excel-Anhang für eigene Auswertungen
- ✅ Übersicht nach Bundesland und Fachbereich

### Beispiel-Benachrichtigung:
```
🎯 NEUE STELLEN GEFUNDEN: 3
📊 GESAMT AKTUELLE STELLEN: 18

NEUE STELLENAUSSCHREIBUNGEN:
🏢 OSZ I Spree-Neiße (Brandenburg)
📋 Lehrkraft Informatik (m/w/d)
📝 Schwerpunkt: Anwendungsentwicklung
🔗 https://osz1spn.de/stellenangebote
📅 04.05.2026
```

## 🚀 Setup (15 Minuten)

### 1. Repository erstellen
- Forken Sie dieses Repository oder erstellen Sie ein neues
- Stellen Sie sicher, dass es **Public** ist (für kostenloses GitHub Actions)

### 2. E-Mail-Konfiguration
Gehen Sie zu **Settings → Secrets and variables → Actions** und fügen Sie hinzu:

```
EMAIL_HOST: smtp.gmail.com
EMAIL_PORT: 587
EMAIL_USER: ihre-email@gmail.com
EMAIL_PASS: ihr-app-passwort
NOTIFY_EMAIL: empfaenger@email.com
```

### 3. Gmail App-Passwort erstellen
1. Google-Konto → Sicherheit
2. 2-Faktor-Authentifizierung aktivieren
3. App-Passwörter → "Mail" auswählen
4. Generiertes Passwort als `EMAIL_PASS` verwenden

### 4. Test-Lauf
- Gehen Sie zu **Actions** → **OSZ Stellenmonitor**
- Klicken Sie **Run workflow**
- Nach ~3 Minuten erhalten Sie die erste E-Mail

## ⚙️ Anpassungen

### Zeitplan ändern
Bearbeiten Sie `.github/workflows/osz-monitor.yml`:
```yaml
schedule:
  - cron: '0 8 * * 1'    # Montag 8:00 UTC
  - cron: '0 8 * * 4'    # + Donnerstag 8:00 UTC
```

### Weitere OSZ hinzufügen
Bearbeiten Sie `scripts/osz_monitor.py`:
```python
OSZ_URLS = {
    'Neues OSZ': 'https://neues-osz.de/stellenangebote',
    # ... weitere URLs
}
```

### Andere E-Mail-Provider
```python
# Outlook
EMAIL_HOST: smtp-mail.outlook.com
EMAIL_PORT: 587

# Yahoo  
EMAIL_HOST: smtp.mail.yahoo.com
EMAIL_PORT: 587
```

## 📈 Monitoring

- **Logs einsehen**: Actions → Workflow-Run → Logs
- **Reports herunterladen**: Actions → Artifacts
- **Fehlerbenachrichtigung**: GitHub sendet E-Mail bei Problemen
- **Datenhistorie**: `data/previous_jobs.json` wird automatisch aktualisiert

## 🔧 Erweiterte Features

Das System kann einfach erweitert werden:

### Slack/Teams Integration
```python
# Slack Webhook statt E-Mail
webhook_url = "https://hooks.slack.com/..."
requests.post(webhook_url, json={"text": message})
```

### Telegram Bot
```python
# Telegram Bot API
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
```

### Keyword-Filter
```python
# Nur bestimmte Fachbereiche
FILTER_KEYWORDS = ['informatik', 'mathematik', 'englisch']
```

### Dashboard mit GitHub Pages
- Automatische HTML-Generierung
- Öffentlich zugängliche Stellenübersicht
- Mobile-optimiert

## 🆘 Troubleshooting

### E-Mail kommt nicht an
- ✅ Spam-Ordner prüfen
- ✅ App-Passwort korrekt eingegeben?
- ✅ 2FA bei Gmail aktiviert?
- ✅ Secrets richtig benannt?

### Workflow läuft nicht
- ✅ Repository ist "Public"?
- ✅ Alle Secrets eingetragen?
- ✅ YAML-Syntax korrekt?

### Zu viele/wenige Benachrichtigungen
- ✅ Zeitplan in Workflow anpassen
- ✅ Schwellenwerte in Python-Script ändern

## 💡 Warum GitHub Actions?

| Kriterium | GitHub Actions | Lokaler Server |
|-----------|----------------|----------------|
| **Kosten** | 0€/Jahr | ~1.400€/Jahr |
| **Verfügbarkeit** | 99.9% | 95-98% |
| **Wartung** | 0 Minuten | 2h/Monat |
| **Setup** | 15 Minuten | 3+ Stunden |

## 📞 Support

Bei Fragen oder Problemen:
1. **Issues** in diesem Repository erstellen
2. **Logs** aus GitHub Actions anhängen
3. **E-Mail-Konfiguration** anonymisiert teilen

## 🔄 Updates

Das System aktualisiert sich automatisch:
- ✅ Neue OSZ-Websites werden erkannt
- ✅ Geänderte Website-Strukturen werden angepasst
- ✅ Verbesserte E-Mail-Templates
- ✅ Zusätzliche Datenquellen

## 📊 Statistiken

Nach dem Setup erhalten Sie:
- **Wöchentliche Berichte** mit Trendanalyse
- **Monatliche Zusammenfassungen** 
- **Jahresübersicht** der OSZ-Stellenentwicklung

---

**🎯 Ziel erreicht**: Nie wieder eine OSZ-Stelle verpassen - vollautomatisch und kostenlos!