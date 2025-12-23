@echo off
echo ================================
echo   DEPLOY MARQUES DESIGN STUDIO
echo ================================
echo.

cd /d "G:\Projeto de IA\generated_sites\marques-design-studio"

echo Verificando Vercel CLI...
where vercel >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Vercel CLI nao encontrado!
    echo Instalando...
    npm install -g vercel
)

echo.
echo Fazendo deploy...
vercel --prod

echo.
echo ================================
echo   DEPLOY CONCLUIDO!
echo ================================
pause
