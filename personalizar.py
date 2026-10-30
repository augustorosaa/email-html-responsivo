from pathlib import Path

html = Path("email.html").read_text(encoding="utf-8")
nome = input("Nome do destinatário: ")

Path("email_personalizado.html").write_text(
    html.replace("{nome}", nome), encoding="utf-8"
)

print("Gerado: email_personalizado.html")