 
>>> if "gopi" in s:
	print("yes gopi in string")

	
yes gopi in string
>>> h=help("modules")

Please wait a moment while I gather a list of all available modules...

__future__          argparse            help_about          search
__main__            array               history             searchbase
_abc                ast                 hmac                searchengine
_aix_support        asynchat            html                secrets
_ast                asyncio             http                select
_asyncio            asyncore            hyperparser         selectors
_bisect             atexit              idle                setuptools
_blake2             audioop             idle_test           shelve
_bootlocale         autocomplete        idlelib             shlex
_bootsubprocess     autocomplete_w      imaplib             shutil
_bz2                autoexpand          imghdr              sidebar
_codecs             base64              imp                 signal
_codecs_cn          bdb                 importlib           site
_codecs_hk          binascii            inspect             smtpd
_codecs_iso2022     binhex              io                  smtplib
_codecs_jp          bisect              iomenu              sndhdr
_codecs_kr          browser             ipaddress           socket
_codecs_tw          builtins            itertools           socketserver
_collections        bz2                 json                sqlite3
_collections_abc    cProfile            keyword             squeezer
_compat_pickle      calendar            lib2to3             sre_compile
_compression        calltip             linecache           sre_constants
_contextvars        calltip_w           locale              sre_parse
_csv                cgi                 logging             ssl
_ctypes             cgitb               lzma                stackviewer
_ctypes_test        chunk               macosx              stat
_datetime           cmath               mailbox             statistics
_decimal            cmd                 mailcap             statusbar
_distutils_hack     code                mainmenu            string
_elementtree        codecontext         marshal             string_ex
_functools          codecs              math                stringprep
_hashlib            codeop              mimetypes           struct
_heapq              collections         mmap                subprocess
_imp                colorizer           modulefinder        sunau
_io                 colorsys            msilib              symbol
_json               compileall          msvcrt              symtable
_locale             concurrent          multicall           sys
_lsprof             config              multiprocessing     sysconfig
_lzma               config_key          netrc               tabnanny
_markupbase         configdialog        nntplib             tarfile
_md5                configparser        nt                  telnetlib
_msi                contextlib          ntpath              tempfile
_multibytecodec     contextvars         nturl2path          test
_multiprocessing    copy                numbers             textview
_opcode             copyreg             opcode              textwrap
_operator           crypt               operator            this
_osx_support        csv                 optparse            threading
_overlapped         ctypes              os                  time
_peg_parser         curses              outwin              timeit
_pickle             dataclasses         parenmatch          tkinter
_py_abc             datetime            parser              token
_pydecimal          dbm                 pathbrowser         tokenize
_pyio               debugger            pathlib             tooltip
_queue              debugger_r          pdb                 trace
_random             debugobj            percolator          traceback
_sha1               debugobj_r          pickle              tracemalloc
_sha256             decimal             pickletools         tree
_sha3               delegator           pip                 tty
_sha512             difflib             pipes               turtle
_signal             dis                 pkg_resources       turtledemo
_sitebuiltins       distutils           pkgutil             types
_socket             doctest             platform            typing
_sqlite3            dynoption           plistlib            undo
_sre                editor              poplib              unicodedata
_ssl                email               posixpath           unittest
_stat               encodings           pprint              urllib
_statistics         ensurepip           profile             uu
_string             enum                pstats              uuid
_strptime           errno               pty                 venv
_struct             faulthandler        py_compile          warnings
_symtable           filecmp             pyclbr              wave
_testbuffer         fileinput           pydoc               weakref
_testcapi           filelist            pydoc_data          webbrowser
_testconsole        fnmatch             pyexpat             while
_testimportmultiple format              pyparse             window
_testinternalcapi   formatter           pyshell             winreg
_testmultiphase     fractions           query               winsound
_thread             ftplib              queue               wsgiref
_threading_local    functools           quopri              xdrlib
_tkinter            gc                  random              xml
_tracemalloc        genericpath         re                  xmlrpc
_uuid               getopt              redirector          xxsubtype
_warnings           getpass             replace             zipapp
_weakref            gettext             reprlib             zipfile
_weakrefset         glob                rlcompleter         zipimport
_winapi             graphlib            rpc                 zlib
_xxsubinterpreters  grep                run                 zoneinfo
_zoneinfo           gzip                runpy               zoomheight
abc                 hashlib             runscript           zzdummy
aifc                heapq               sched               
antigravity         help                scrolledlist        

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".


>>> m="""__future__          argparse            help_about          search
__main__            array               history             searchbase
_abc                ast                 hmac                searchengine
_aix_support        asynchat            html                secrets
_ast                asyncio             http                select
_asyncio            asyncore            hyperparser         selectors
_bisect             atexit              idle                setuptools
_blake2             audioop             idle_test           shelve
_bootlocale         autocomplete        idlelib             shlex
_bootsubprocess     autocomplete_w      imaplib             shutil
_bz2                autoexpand          imghdr              sidebar
_codecs             base64              imp                 signal
_codecs_cn          bdb                 importlib           site
_codecs_hk          binascii            inspect             smtpd
_codecs_iso2022     binhex              io                  smtplib
_codecs_jp          bisect              iomenu              sndhdr
_codecs_kr          browser             ipaddress           socket
_codecs_tw          builtins            itertools           socketserver
_collections        bz2                 json                sqlite3
_collections_abc    cProfile            keyword             squeezer
_compat_pickle      calendar            lib2to3             sre_compile
_compression        calltip             linecache           sre_constants
_contextvars        calltip_w           locale              sre_parse
_csv                cgi                 logging             ssl
_ctypes             cgitb               lzma                stackviewer
_ctypes_test        chunk               macosx              stat
_datetime           cmath               mailbox             statistics
_decimal            cmd                 mailcap             statusbar
_distutils_hack     code                mainmenu            string
_elementtree        codecontext         marshal             string_ex
_functools          codecs              math                stringprep
_hashlib            codeop              mimetypes           struct
_heapq              collections         mmap                subprocess
_imp                colorizer           modulefinder        sunau
_io                 colorsys            msilib              symbol
_json               compileall          msvcrt              symtable
_locale             concurrent          multicall           sys
_lsprof             config              multiprocessing     sysconfig
_lzma               config_key          netrc               tabnanny
_markupbase         configdialog        nntplib             tarfile
_md5                configparser        nt                  telnetlib
_msi                contextlib          ntpath              tempfile
_multibytecodec     contextvars         nturl2path          test
_multiprocessing    copy                numbers             textview
_opcode             copyreg             opcode              textwrap
_operator           crypt               operator            this
_osx_support        csv                 optparse            threading
_overlapped         ctypes              os                  time
_peg_parser         curses              outwin              timeit
_pickle             dataclasses         parenmatch          tkinter
_py_abc             datetime            parser              token
_pydecimal          dbm                 pathbrowser         tokenize
_pyio               debugger            pathlib             tooltip
_queue              debugger_r          pdb                 trace
_random             debugobj            percolator          traceback
_sha1               debugobj_r          pickle              tracemalloc
_sha256             decimal             pickletools         tree
_sha3               delegator           pip                 tty
_sha512             difflib             pipes               turtle
_signal             dis                 pkg_resources       turtledemo
_sitebuiltins       distutils           pkgutil             types
_socket             doctest             platform            typing
_sqlite3            dynoption           plistlib            undo
_sre                editor              poplib              unicodedata
_ssl                email               posixpath           unittest
_stat               encodings           pprint              urllib
_statistics         ensurepip           profile             uu
_string             enum                pstats              uuid
_strptime           errno               pty                 venv
_struct             faulthandler        py_compile          warnings
_symtable           filecmp             pyclbr              wave
_testbuffer         fileinput           pydoc               weakref
_testcapi           filelist            pydoc_data          webbrowser
_testconsole        fnmatch             pyexpat             while
_testimportmultiple format              pyparse             window
_testinternalcapi   formatter           pyshell             winreg
_testmultiphase     fractions           query               winsound
_thread             ftplib              queue               wsgiref
_threading_local    functools           quopri              xdrlib
_tkinter            gc                  random              xml
_tracemalloc        genericpath         re                  xmlrpc
_uuid               getopt              redirector          xxsubtype
_warnings           getpass             replace             zipapp
_weakref            gettext             reprlib             zipfile
_weakrefset         glob                rlcompleter         zipimport
_winapi             graphlib            rpc                 zlib
_xxsubinterpreters  grep                run                 zoneinfo
_zoneinfo           gzip                runpy               zoomheight
abc                 hashlib             runscript           zzdummy
aifc                heapq               sched               
antigravity         help                scrolledlist        

"""

>>> l="string re difflib textwrap unicodedata stringprep readline rlcompleter"
>>> f=l.split(" ")
>>> f
['string', 're', 'difflib', 'textwrap', 'unicodedata', 'stringprep', 'readline', 'rlcompleter']
>>> for i in f:
	print(i)

	
string
re
difflib
textwrap
unicodedata
stringprep
readline
rlcompleter
>>> for i in f:
	if i in m:
		print(i,'is in list')
	else:
		print(i,'not in list')

		
string is in list
re is in list
difflib is in list
textwrap is in list
unicodedata is in list
stringprep is in list
readline not in list
rlcompleter is in list
>>> 
KeyboardInterrupt
>>> 
