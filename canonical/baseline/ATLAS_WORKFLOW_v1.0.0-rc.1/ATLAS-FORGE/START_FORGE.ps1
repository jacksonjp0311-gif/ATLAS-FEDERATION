$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$env:PYTHONPATH = Join-Path $PSScriptRoot "src"
py -3 -m atlas_forge serve
if ($LASTEXITCODE -ne 0) { throw "Forge exited with code $LASTEXITCODE" }
