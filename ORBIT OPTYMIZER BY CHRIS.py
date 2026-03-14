import customtkinter as ctk
import os
import subprocess
import ctypes

def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

ctk.set_appearance_mode("Dark")

class OrbitOptimizer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ORBIT OPTIMIZER BY CHRIS")
        self.geometry("600x750")
        
        # Panel główny (Skeumorfizm: cienie i obramowanie)
        self.panel = ctk.CTkFrame(self, corner_radius=40, border_width=4, border_color="#1A1A1A", fg_color="#0D0D0D")
        self.panel.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.panel, text="ORBIT OPTIMIZER", font=("Impact", 40), text_color="#00D2FF")
        self.label.pack(pady=15)
        
        self.sub_label = ctk.CTkLabel(self.panel, text="BY CHRIS", font=("Arial", 14, "italic"), text_color="#555555")
        self.sub_label.pack(pady=0)

        # Logi (Terminal wewnątrz aplikacji)
        self.log_box = ctk.CTkTextbox(self.panel, height=150, corner_radius=15, fg_color="#000000", text_color="#00FF00", font=("Consolas", 11))
        self.log_box.pack(pady=20, padx=30, fill="x")
        self.log_write("System gotowy do optymalizacji...")

        # Przycisk EXTREME BOOST (Skeumorficzny, wypukły)
        self.boost_btn = ctk.CTkButton(self.panel, text="EXTREME BOOST", 
                                       font=("Arial", 22, "bold"),
                                       height=80, width=350,
                                       corner_radius=40,
                                       fg_color="#CC0000", hover_color="#FF0000",
                                       border_width=2, border_color="#550000",
                                       command=self.run_boost)
        self.boost_btn.pack(pady=20)

        # Przycisk REVERT (Cofanie zmian)
        self.revert_btn = ctk.CTkButton(self.panel, text="COFNIJ ZMIANY (REVERT)", 
                                        font=("Arial", 14),
                                        height=40, width=200,
                                        corner_radius=20,
                                        fg_color="#333333", hover_color="#444444",
                                        command=self.revert_changes)
        self.revert_btn.pack(pady=10)

    def log_write(self, message):
        self.log_box.insert("end", f"> {message}\n")
        self.log_box.see("end")
        self.update()

    def run_boost(self):
        if not is_admin():
            self.log_write("BŁĄD: URUCHOM JAKO ADMIN!")
            return

        self.log_write("TWORZENIE PUNKTU PRZYWRACANIA...")
        os.system('checkpoint-computer -description "OrbitOptimizerBackup" -restorepointtype "MODIFY_SETTINGS"')

        # 1. SWAP OFF
        self.log_write("USUWANIE SWAP (PAGEFILE)...")
        os.system('wmic computersystem where name="%computername%" set AutomaticManagedPagefile=False')
        os.system('wmic pagefileset where name="C:\\\\pagefile.sys" delete')

        # 2. ANTIVIRUS & UPDATE OFF
        self.log_write("WYŁĄCZANIE DEFENDERA I WINDOWS UPDATE...")
        os.system('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d 1 /f')
        os.system('sc config wuauserv start= disabled')
        os.system('sc stop wuauserv')

        # 3. TELEMETRIA & ZBĘDNE USŁUGI (Lista agresywna)
        self.log_write("CZYSZCZENIE ZBĘDNYCH USŁUG (XBOX, DRUKARKI, MAPY)...")
        services = ["DiagTrack", "dmwappushservice", "SysMain", "PrintSpooler", "XblAuthManager", "XblGameSave", "MapsBroker"]
        for s in services:
            os.system(f'sc stop {s} >nul 2>&1')
            os.system(f'sc config {s} start= disabled >nul 2>&1')

        # 4. PING & SPEED TEST (Network Tweak)
        self.log_write("OPTYMALIZACJA PINGU I SIECI...")
        os.system('netsh int tcp set global autotuninglevel=disabled')
        os.system('netsh int tcp set global chimney=enabled')
        os.system('netsh int tcp set global rss=enabled')

        # 5. AUTOSTART CLEANUP
        self.log_write("CZYSZCZENIE AUTOSTARTU...")
        os.system('reg delete "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /va /f')

        # 6. WYSOKI PRIORYTET
        self.log_write("USTAWIANIE PRIORYTETU WYSOKIEGO...")
        os.system('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d 0 /f')

        self.log_write("--- OPTYMALIZACJA ZAKOŃCZONA! ZRESTARTUJ PC ---")

    def revert_changes(self):
        self.log_write("PRZYWRACANIE USTAWIEŃ DOMYŚLNYCH...")
        os.system('sc config wuauserv start= auto')
        os.system('sc config DiagTrack start= auto')
        os.system('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d 0 /f')
        self.log_write("ZRESTARTUJ PC, ABY WRÓCIĆ DO NORMY.")

if __name__ == "__main__":
    app = OrbitOptimizer()
    app.mainloop()