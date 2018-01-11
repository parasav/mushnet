# -*- mode: python -*-

block_cipher = None


a = Analysis(['arangui.py'],
             pathex=['C:\\Users\\Parker\\Documents\\Github\\mushnet'],
             binaries=[],
             datas=[('C:\\Users\\Parker\\Envs\\mushnet\\lib\\site-packages\\eel\\eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket', 'arango'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='arangui',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
