from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/form", methods=["GET", "POST"])
def form():
    message = None
    if request.method == "POST":
        prenom = request.form.get("prenom")
        nom = request.form.get("nom")
        email = request.form.get("email")
        sujet = request.form.get("sujet")
        message_texte = request.form.get("message")
        consentement = request.form.get("consentement")

        if prenom and nom and "@" in email and consentement:
            message = f"Merci {prenom} {nom}, votre message a bien été envoyé concernant : {sujet}."
        else:
            message = "Erreur dans le formulaire. Veuillez remplir tous les champs obligatoires."
    return render_template("form.html", message=message)
