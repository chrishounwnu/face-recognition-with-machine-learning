Workflow :
1️⃣ Capturer une image en direct (capture.py)
2️⃣ Prétraiter cette image (détection + alignement du visage) (preprocess.py)
3️⃣ Créer des embeddings pour les images dans dataset/ (recognition.py)
4️⃣ Comparer l’image capturée avec celles du dataset pour identification (main.py)

Comment ca fonctionne ?
✅ Quand quelqu'un se place devant la webcam, le programme compare l'image capturée aux images du dataset.
✅ Si une correspondance est trouvée, il affiche son nom, âge et d'autres informations.
✅ Sinon, il indique "Unknown face" et propose d'ajouter la personne au dataset.

🛠 Étapes du Projet :
1️⃣ Capture de l’image en direct (capture.py) → 
2️⃣ Prétraitement (preprocess.py) → Détection et normalisation du visage.
3️⃣ Création des embeddings (recognition.py) → Générer une signature numérique du visage.
4️⃣ Comparaison et identification (recognition.py) → Trouver la personne dans le dataset.
5️⃣ Affichage des informations sur l’écran.
