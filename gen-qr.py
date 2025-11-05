import qrcode
import os
import sys

def main():
    print("=== Générateur de QR Code ===\n")

    # Chemin du dossier de l'exécutable ou du script
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Création du dossier QR_Codes
    output_dir = os.path.join(base_dir, "QR_Codes")
    os.makedirs(output_dir, exist_ok=True)

    # Lien à encoder
    data = input("Lien ou texte à encoder : ").strip()
    if not data:
        print("Erreur : lien vide")
        return

    # Niveau de correction
    correction = input("Niveau de correction [L=7%, M=15%, Q=25%, H=30%] (défaut=M) : ").upper() or "M"
    if correction not in ["L", "M", "Q", "H"]:
        print("Erreur : niveau invalide, utilisation de M")
        correction = "M"

    correction_levels = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H
    }

    # Taille du module
    try:
        size = int(input("Taille du QR (module) [défaut=10] : ").strip() or 10)
    except ValueError:
        size = 10

    # Marge
    try:
        margin = int(input("Marge autour du QR [défaut=4] : ").strip() or 4)
    except ValueError:
        margin = 4

    # Nom du fichier
    filename = input("Nom du fichier PNG [défaut=qr_code.png] : ").strip() or "qr_code.png"
    filepath = os.path.join(output_dir, filename)

    # Création du QR
    qr = qrcode.QRCode(
        version=None,
        error_correction=correction_levels[correction],
        box_size=size,
        border=margin
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    print(f"\n✅ QR code créé avec succès dans : {filepath}")

if __name__ == "__main__":
    main()
