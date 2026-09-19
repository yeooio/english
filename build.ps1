$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$buildDirectory = Join-Path $projectRoot 'build'

New-Item -ItemType Directory -Path $buildDirectory -Force | Out-Null
Push-Location $projectRoot
try {
    latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
    if ($LASTEXITCODE -ne 0) { throw "latexmk failed with exit code $LASTEXITCODE" }
}
finally {
    Pop-Location
}
