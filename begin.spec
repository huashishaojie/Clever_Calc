# -*- mode: python -*-
import sys
sys.setrecursionlimit(100000)
block_cipher = None

a = Analysis(['begin.py'],
             pathex=['G:\\Anaconda\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'G:\\Project\\project1.0'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='begin',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='calculator.ico')
