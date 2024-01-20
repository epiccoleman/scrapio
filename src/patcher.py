import os

class Patcher:
    def __init__(self, clean_rom_path, hack_path, multipatch_path):
        self.clean_rom_path = clean_rom_path
        self.hack_path = hack_path
        self.multipatch_path = multipatch_path

    def find_bps_file(self):
        for root, dirs, files in os.walk(self.hack_path):
            for file in files:
                if file.endswith(".bps"):
                    return os.path.join(root, file)
        return None
