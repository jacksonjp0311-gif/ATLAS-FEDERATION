<#[
ATLAS FORGE — offline model-to-STL demonstration.
Requires Python 3.10+ already installed locally. No network/downloads.
The local slicer/printer must be separately configured; this does not issue G-code.
#>
param(
    [Parameter(Mandatory=$true)][string]$AtlasRoot,
    [string]$OutputDir = '.\ATLAS_PRINT_OUTPUT',
    [double]$BoreMm = 8.4,
    [double]$CoreMm = 16.0,
    [double]$FlangeMm = 40.0
)
$ErrorActionPreference = 'Stop'
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not (Test-Path (Join-Path $AtlasRoot 'tools\atlas_offline.py'))) {
    throw 'Expected extracted full Atlas folder; offline reader not found.'
}
$Script = Join-Path $Here 'atlas_print_bridge.py'
$Verifier = Join-Path $Here 'verify_mesh.py'
& py -3 $Script --atlas-root $AtlasRoot --out $OutputDir --bore-mm $BoreMm --core-mm $CoreMm --flange-mm $FlangeMm
if ($LASTEXITCODE -ne 0) { throw 'Offline design generation failed' }
$Stl = Join-Path $OutputDir 'ATLAS_COIL_FORMER.stl'
$Audit = Join-Path $OutputDir 'MESH_AUDIT.json'
& py -3 $Verifier $Stl --width $FlangeMm --out $Audit
if ($LASTEXITCODE -ne 0) { throw 'STL geometry audit failed' }
Write-Output "Digital STL verified. Review $Audit and slice $Stl locally using your known printer profile. No physical printer operation has occurred."
