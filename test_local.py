#!/usr/bin/env python3
"""
Lokaler Test des OSZ Monitors - Führen Sie dies aus, um das System zu testen
bevor Sie es auf GitHub Actions deployen.
"""

import os
import sys
sys.path.append('scripts')

# Setze Test-Umgebungsvariablen (ersetzen Sie mit Ihren echten Werten für Tests)
os.environ['EMAIL_HOST'] = 'smtp.gmail.com'
os.environ['EMAIL_PORT'] = '587'
os.environ['EMAIL_USER'] = 'test@gmail.com'  # Ihre E-Mail
os.environ['EMAIL_PASS'] = 'test-password'   # Ihr App-Passwort
os.environ['NOTIFY_EMAIL'] = 'test@gmail.com'  # Empfänger-E-Mail

# Importiere und führe Monitor aus
from osz_monitor import OSZMonitor

def test_scraping_only():
    """Testet nur das Scraping ohne E-Mail-Versand"""
    print("🧪 Teste OSZ Monitor (nur Scraping)...")
    
    monitor = OSZMonitor()
    
    # Lade vorherige Daten
    previous_data = monitor.load_previous_data()
    print(f"📂 Vorherige Daten geladen: {len(previous_data.get('jobs', []))} Stellen")
    
    # Scrape aktuelle Daten
    monitor.scrape_all_sources()
    print(f"🔍 Aktuelle Daten gescraped: {len(monitor.all_jobs)} Stellen")
    
    # Erstelle Excel-Report
    excel_file = monitor.create_excel_report()
    print(f"📊 Excel-Report erstellt: {excel_file}")
    
    # Vergleiche mit vorherigen Daten
    has_changes = monitor.compare_with_previous(previous_data)
    print(f"🆕 Neue Stellen gefunden: {len(monitor.new_jobs)}")
    
    # Zeige gefundene Stellen
    print("\n📋 GEFUNDENE STELLEN:")
    print("=" * 50)
    for job in monitor.all_jobs:
        print(f"🏢 {job['source']} ({job['location']})")
        print(f"📋 {job['title']}")
        print(f"📝 {job['description']}")
        print("-" * 30)
    
    if monitor.new_jobs:
        print(f"\n🆕 NEUE STELLEN ({len(monitor.new_jobs)}):")
        print("=" * 50)
        for job in monitor.new_jobs:
            print(f"🏢 {job['source']} ({job['location']})")
            print(f"📋 {job['title']}")
            print(f"📝 {job['description']}")
            print("-" * 30)
    
    return {
        'total_jobs': len(monitor.all_jobs),
        'new_jobs': len(monitor.new_jobs),
        'excel_file': excel_file,
        'has_changes': has_changes
    }

def test_full_system():
    """Testet das komplette System inklusive E-Mail"""
    print("🧪 Teste komplettes OSZ Monitor System...")
    print("⚠️  ACHTUNG: Dies sendet eine echte E-Mail!")
    
    confirm = input("Möchten Sie fortfahren? (j/N): ")
    if confirm.lower() != 'j':
        print("❌ Test abgebrochen")
        return
    
    monitor = OSZMonitor()
    result = monitor.run()
    
    print(f"\n✅ Test abgeschlossen:")
    print(f"📊 Gefundene Stellen: {result['total_jobs']}")
    print(f"🆕 Neue Stellen: {result['new_jobs']}")
    print(f"📧 E-Mail gesendet: {result['notification_sent']}")
    print(f"📁 Excel-Datei: {result['excel_file']}")

if __name__ == "__main__":
    print("🎯 OSZ Monitor - Lokaler Test")
    print("=" * 40)
    print("1. Nur Scraping testen (keine E-Mail)")
    print("2. Komplettes System testen (mit E-Mail)")
    print("3. Beenden")
    
    choice = input("\nWählen Sie eine Option (1-3): ")
    
    if choice == "1":
        result = test_scraping_only()
        print(f"\n✅ Scraping-Test abgeschlossen: {result}")
    elif choice == "2":
        test_full_system()
    else:
        print("👋 Auf Wiedersehen!")