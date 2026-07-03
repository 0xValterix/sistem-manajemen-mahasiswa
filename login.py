# login.py

from getpass import getpass

akun = {
    "admin": "admin123"
}


def login():
    """Fungsi untuk login."""

    print("\n===== LOGIN =====")
    username = input("Username : ")
    password = getpass("Password : ")

    if username in akun and akun[username] == password:
        print("Login berhasil!")
        return True

    print("Username atau password salah!")
    return False


def logout():
    """Fungsi untuk logout."""

    print("Logout berhasil.")

# Test fitur login logout
if __name__ == "__main__":
    if login():
        logout()