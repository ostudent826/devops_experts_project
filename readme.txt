install helm to windows:

use powershell as admin:
        "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        "

verify choco open cmd write :
        "choco"

install helm via powershell:

        "choco install kubernetes-helm"

add helm to windows path:

        # Get the current PATH
        $currentPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::Machine)

        # Add the new path if it doesn't already exist
        if ($currentPath -notlike "*C:\ProgramData\chocolatey\bin*") {
            $newPath = $currentPath + ";C:\ProgramData\chocolatey\bin"
            [Environment]::SetEnvironmentVariable("Path", $newPath, [EnvironmentVariableTarget]::Machine)
        }

        # Confirm the PATH variable
        [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::Machine)
