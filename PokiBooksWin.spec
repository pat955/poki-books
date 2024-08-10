# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    [('src/poki_books.py'),
    ],
    pathex=[],
    binaries=[],
    datas=[
        ('static/*', 'static')  # Ensure static files go into a 'static' folder
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

splash = Splash('static/image.png',
    always_on_top=False,
    binaries=a.binaries,
    datas=a.datas,
    text_pos=(10, 50),
    text_size=12,
    text_color='black')

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    splash,
    a.scripts,
    [],
    name='PokiBooks.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['static/icon.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PokiBooksWin'
)
