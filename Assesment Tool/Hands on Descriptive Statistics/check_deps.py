import importlib.util
for pkg in ['numpy', 'scipy', 'pandas']:
    spec = importlib.util.find_spec(pkg)
    print(f'{pkg}:', 'installed' if spec else 'missing')
