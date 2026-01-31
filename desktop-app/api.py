import requests

BASE_URL = "http://127.0.0.1:8000/api"
TOKEN = None  # will be set after login


def set_token(token):
    global TOKEN
    TOKEN = token


def get_headers():
    return {"Authorization": f"Token {TOKEN}"} if TOKEN else {}


# ================= LOGIN =================
def login(username, password):
    try:
        response = requests.post(
            f"{BASE_URL}/login/",
            json={"username": username, "password": password},
        )
        response.raise_for_status()
        data = response.json()
        set_token(data["token"])
        return True
    except Exception as e:
        print("Login error:", e)
        return False


# ================= SUMMARY =================
def get_summary():
    try:
        response = requests.get(f"{BASE_URL}/summary/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching summary:", e)
        return None


# ================= EQUIPMENT =================
def get_equipment_list():
    try:
        response = requests.get(f"{BASE_URL}/equipment/", headers=get_headers())
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching equipment:", e)
        return []


# ================= CSV UPLOAD (FIXED) =================
def upload_csv(file_path):
    try:
        with open(file_path, "rb") as f:
            response = requests.post(
                f"{BASE_URL}/upload/",   # ✅ CORRECT URL
                headers=get_headers(),
                files={"file": f},
            )

        response.raise_for_status()
        return True
    except Exception as e:
        print("Error uploading CSV:", e)
        return False


# ================= PDF DOWNLOAD =================
def download_pdf_report(save_path):
    try:
        url = f"{BASE_URL}/download-report/"
        response = requests.get(url, headers=get_headers())

        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            return True
        return False
    except Exception as e:
        print("Error:", e)
        return False
