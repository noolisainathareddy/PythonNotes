import shutil
from importlib.metadata import files
from pathlib import Path
from datetime import datetime

def backup_files(str_dir):
    files = sorted(Path(str_dir).glob('*.log'), key=lambda f: f.stat().st_mtime)
    new_file=files[-1]
    print(new_file)
    print(new_file.suffix)

    for i in files[:-5]:
        print(i)
    print("---------------------")
    src = Path(str_dir)
    ts = datetime.now().strftime('%y_%m_%d_%H_%M_%S')
    print(src.with_name(f'{src.name}.{ts}'))

    # shutil.copy2(new_file, )

backup_files("/Users/sainooli/Desktop/DevOps_Resume/Interview Prep/Linux_Prep/BashScript/Basic/Test")
