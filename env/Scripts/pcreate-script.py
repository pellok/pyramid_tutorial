#!D:\Python\Pyramid\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyramid==1.5.7','console_scripts','pcreate'
__requires__ = 'pyramid==1.5.7'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pyramid==1.5.7', 'console_scripts', 'pcreate')()
    )