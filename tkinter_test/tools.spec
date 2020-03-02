# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['tools.py'],
             pathex=['H:\\pycharm\\tools\\tkinter_test'],
             binaries=[],
             datas=[('phone/phone.dat','tkinter_test/phone'),
                    ('idcard/id','tkinter_test/idcard'),
                    ('idcard/pic.gif','tkinter_test/idcard'),
                    ('aaa.ico','tkinter_test/idcard')
             ],
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
          name='tools',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='aaa.ico')
