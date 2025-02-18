import ctypes

try:
    mariadb_lib = ctypes.CDLL('/Users/chino0207/Desktop/Python Projects/server/pyweb/.venv/lib/python3.9/site-packages/mariadb/_mariadb.cpython-39-darwin.so')
    mariadb_lib._mysql_ps_fetch_functions  # Attempt to access the symbol
    print("Symbol '_mysql_ps_fetch_functions' is found.")
except AttributeError:
    print("Symbol '_mysql_ps_fetch_functions' not found.")
except OSError as e:
    print(f"Error loading shared object: {e}")
