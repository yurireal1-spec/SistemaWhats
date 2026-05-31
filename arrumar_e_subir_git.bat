@echo off
echo ==========================================
echo Configurando e preparando o repositorio Git...
echo ==========================================

REM 1. Remover o cache do wppconnect-server no Git
git rm --cached -r wppconnect-server

REM 2. Remover atributos de somente leitura e oculto da pasta .git do wppconnect-server
attrib -R -H -S wppconnect-server\.git /S /D

REM 3. Apagar a pasta .git interna do wppconnect-server
rmdir /s /q wppconnect-server\.git

REM 4. Configurar autocrlf para evitar os avisos de LF/CRLF
git config core.autocrlf true

echo ==========================================
echo Adicionando os arquivos ao Git...
echo ==========================================
git add .

echo ==========================================
echo Criando o commit...
echo ==========================================
git commit -m "Upload completo do projeto (incluindo wppconnect-server)"

echo ==========================================
echo Enviando para o GitHub...
echo ==========================================
git push origin main

echo ==========================================
echo Concluido!
echo ==========================================
pause
