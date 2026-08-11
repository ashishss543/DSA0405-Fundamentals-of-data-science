from pathlib import Path
import subprocess

BASE = Path(__file__).resolve().parent
OUTPUT_DIR = BASE / 'output'
OUTPUT_DIR.mkdir(exist_ok=True)

scripts = [
    ('q1_mean.py', 'q1_mean.txt'),
    ('q2_median.py', 'q2_median.txt'),
    ('q3_mode.py', 'q3_mode.txt'),
    ('q4_range.py', 'q4_range.txt'),
    ('q5_variance.py', 'q5_variance.txt'),
    ('q6_std_dev.py', 'q6_std_dev.txt'),
    ('q7_statistics_module.py', 'q7_statistics_module.txt'),
    ('q8_numpy_library.py', 'q8_numpy_library.txt'),
    ('q9_scipy_mode.py', 'q9_scipy_mode.txt'),
    ('q10_pandas_summary.py', 'q10_pandas_summary.txt'),
]

for script, outname in scripts:
    script_path = BASE / script
    out_path = OUTPUT_DIR / outname
    print(f'Running {script} -> {out_path.name}')
    result = subprocess.run([
        'C:/Users/asish/AppData/Local/Python/pythoncore-3.14-64/python.exe',
        str(script_path)
    ], capture_output=True, text=True)
    out_path.write_text(result.stdout)
    if result.stderr:
        print(f'ERROR in {script}:', result.stderr)
