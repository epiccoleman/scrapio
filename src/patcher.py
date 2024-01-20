import os

class Patcher:
    def __init__(self, clean_rom_path, hack_path):
        self.clean_rom_path = clean_rom_path
        self.hack_path = hack_path

    def find_bps_file(self):
        for file in os.listdir(self.hack_path):
            if file.endswith(".bps"):
                return os.path.join(self.hack_path, file)
        return None
