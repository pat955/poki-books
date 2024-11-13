# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    [('src/poki_books.py'),
    ],
    pathex=[],
    binaries=[],
    datas=[
        ('static/*', 'static')  # Ensure static files go into a 'static' folder| add readme
    ],
    hiddenimports=[
        ('src/gopy'),
    ],
    hookspath=[],
    runtime_hooks=[],
    hooksconfig={},
    excludes=[],
    noarchive=False,
    optimize=0,
)



pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PokiBooks.app',
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
    icon='static/icon.png',
)

app = BUNDLE(exe,
    name='PokiBooks.app',
    icon='static/icon.png',
    bundle_identifier='com.pat955.pokibooks',
    version='0.0.1',
    info_plist='./Info.plist'
    )


coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PokiBooksMacOs'
)

