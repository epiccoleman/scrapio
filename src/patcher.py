import os
import subprocess

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

    def patch_rom(self):
        patch_file = self.find_bps_file()
        if patch_file is None:
            print("No .bps file found in hack_path.")
            return

        output_name = os.path.basename(self.hack_path)
        subprocess.run([self.multipatch_path, "--apply", patch_file, self.clean_rom_path, f"{self.hack_path}/{output_name}.smc"])
