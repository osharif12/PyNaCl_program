# -*- mode: python -*-

block_cipher = None


a = Analysis(['ransomware.py'],
             pathex=['/Users/omarsharif/IdeaProjects/USF/CS 683 (Computer Security)/PyNaCl_program'],
             binaries=[],
             datas=[],
             hiddenimports=['_cffi_backend'],
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
          name='ransomware',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='ransomware.app',
             icon=None,
             bundle_identifier=None)
