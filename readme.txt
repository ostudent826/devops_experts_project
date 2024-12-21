install helm to windows:

use powershell as admin:
"Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
"

verify choco open cmd write :
"choco"

install helm via powershell:

"choco install kubernetes-helm"

