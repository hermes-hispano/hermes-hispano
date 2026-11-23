#!/usr/bin/env python3
"""Comprobaciones de Hermes Hispano: formato de guías y habilidades, y claves filtradas."""
import pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
errores = []

SECRETOS = {
    "un token de GitHub": r"gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{50,}",
    "una clave de OpenAI": r"sk-(proj-)?[A-Za-z0-9_-]{32,}",
    "una clave de Anthropic": r"sk-ant-[A-Za-z0-9_-]{32,}",
    "una clave de OpenRouter": r"sk-or-v1-[a-f0-9]{48,}",
    "una clave de AWS": r"AKIA[0-9A-Z]{16}",
    "una clave de Google": r"AIza[0-9A-Za-z_-]{35}",
    "un token de bot de Telegram": r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b",
    "una clave privada": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
}

def cabecera(texto):
    m = re.match(r"^---\n(.*?)\n---", texto, re.S)
    if not m:
        return None
    datos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            k, v = linea.split(":", 1)
            datos[k.strip()] = v.split("#")[0].strip().strip('"')
    return datos

for f in RAIZ.rglob("*"):
    if not f.is_file() or ".git" in f.parts or f.suffix in {".png", ".jpg", ".svg", ".ico"}:
        continue
    if f.name == "validar.py":
        continue
    try:
        texto = f.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for nombre, patron in SECRETOS.items():
        if re.search(patron, texto):
            errores.append(f"{f.relative_to(RAIZ)}: parece contener {nombre}. Quítalo y revócalo cuanto antes.")

for f in (RAIZ / "guias").glob("*.md"):
    if f.name == "README.md":
        continue
    c = cabecera(f.read_text(encoding="utf-8"))
    if c is None:
        errores.append(f"{f.relative_to(RAIZ)}: falta la cabecera (ver CONTRIBUTING.md).")
        continue
    for campo in ("titulo", "etiqueta", "version_hermes", "modelo", "sistema", "fecha"):
        if not c.get(campo):
            errores.append(f"{f.relative_to(RAIZ)}: falta el campo «{campo}» en la cabecera.")
    if c.get("etiqueta") not in ("probado", "datos-publicos"):
        errores.append(f"{f.relative_to(RAIZ)}: la etiqueta debe ser «probado» o «datos-publicos».")

for d in (RAIZ / "skills").iterdir() if (RAIZ / "skills").exists() else []:
    if not d.is_dir():
        continue
    skill = d / "SKILL.md"
    if not skill.exists():
        errores.append(f"skills/{d.name}: falta SKILL.md.")
        continue
    c = cabecera(skill.read_text(encoding="utf-8")) or {}
    if c.get("name") != d.name:
        errores.append(f"skills/{d.name}/SKILL.md: «name» debe ser igual al nombre de la carpeta.")
    if not c.get("description") or len(c["description"]) >= 1024:
        errores.append(f"skills/{d.name}/SKILL.md: «description» es obligatoria y debe tener menos de 1024 caracteres.")
    if not (d / "pruebas.md").exists():
        errores.append(f"skills/{d.name}: falta pruebas.md con las tareas de prueba.")

if errores:
    print("Hay cosas que corregir:\n")
    print("\n".join(f"- {e}" for e in errores))
    sys.exit(1)
print("Todo correcto.")
