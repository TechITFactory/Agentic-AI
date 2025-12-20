<#
.SYNOPSIS
  Sets up a local Python virtual environment for Agentic-AI and installs dependencies.

.DESCRIPTION
  This is meant to be a student-friendly, copy/paste runnable setup script for Windows PowerShell.
  It creates `venv/` (if missing), activates it, upgrades pip, installs requirements, and runs
  a quick verification.

.NOTES
  Run from the repo root:
    PS> .\scripts\setup.ps1
#>

$ErrorActionPreference = 'Stop'

function Write-Step([string]$Message) {
  Write-Host "`n==> $Message" -ForegroundColor Cyan
}

Write-Step "Validating repo root"
if (-not (Test-Path -Path '.\requirements.txt')) {
  throw "requirements.txt not found. Run this from the Agentic-AI repo root."
}

Write-Step "Creating virtual environment (venv) if needed"
if (-not (Test-Path -Path '.\venv')) {
  python -m venv venv
}

Write-Step "Activating venv"
. .\venv\Scripts\Activate.ps1

Write-Step "Upgrading pip"
python -m pip install --upgrade pip

Write-Step "Installing dependencies"
pip install -r .\requirements.txt

Write-Step "Verifying environment"
python .\scripts\verify_env.py

Write-Host "`nSetup complete." -ForegroundColor Green
