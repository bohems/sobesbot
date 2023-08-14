import subprocess

def is_package_installed(package_name):
    try:
        subprocess.run(["pip", "show", package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package_name):      
    if not is_package_installed(package_name):        
        subprocess.check_call(["pip", "install", package_name])
        print(f"Пакет {package_name} успешно установлен")
    else:
        print(f"Пакет {package_name} уже был ранее установлен.")
