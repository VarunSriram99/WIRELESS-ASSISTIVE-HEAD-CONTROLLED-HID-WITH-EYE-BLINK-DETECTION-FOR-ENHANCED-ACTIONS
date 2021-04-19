# -*- mode: python -*-

block_cipher = None


a = Analysis(['test3.py'],
             pathex=['C:\\Windows\\System32\\downlevel', 'C:\\Users\\S Varun\\Desktop\\test\\test3'],
             binaries=[('C:\\Users\\S Varun\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\pvporcupine\\resources\\keyword_files\\windows\\*', 'pvporcupine\\resources\\keyword_files\\windows'),('C:\\Users\\S Varun\\AppData\\Local\\Programs\\Python\\Python37\\\\Lib\\site-packages\\pvporcupine\\lib\\windows\\amd64\\*', 'pvporcupine\\lib\\windows\\amd64'),('C:\\Users\\S Varun\\AppData\\Local\\Programs\\Python\\Python37\\\\Lib\\site-packages\\pvporcupine\\lib\\common\\*', 'pvporcupine\\lib\\common')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('v', None, 'OPTION')],
          name='test3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
