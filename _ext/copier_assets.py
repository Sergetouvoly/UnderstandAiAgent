"""Copie le dossier assets/ dans le site final.

Les notebooks affichent leurs schémas avec des balises HTML <img src="assets/...">.
Sphinx ne copie pas ces fichiers tout seul : on les recopie à la fin de la
construction, à l'emplacement que les chemins relatifs des pages attendent.
"""
import shutil
from pathlib import Path

DOSSIERS = ("assets",)
SUFFIXES = {".png", ".svg", ".csv", ".md", ".txt"}  # les sources .excalidraw restent dans le dépôt


def copier(app, exception):
    if exception or app.builder.format != "html":
        return
    for nom in DOSSIERS:
        source = Path(app.srcdir) / nom
        for fichier in source.rglob("*"):
            if fichier.suffix.lower() in SUFFIXES:
                cible = Path(app.outdir) / nom / fichier.relative_to(source)
                cible.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(fichier, cible)


def setup(app):
    app.connect("build-finished", copier)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
