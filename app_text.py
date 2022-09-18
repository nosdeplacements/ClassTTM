#!/usr/bin/env python3

import numpy as np

# Initialize the arrays
reponse  = np.full((9,), None)
question = np.full((9,), None)
consigne = np.full((5,), None)

# Questions
question[0] = u"Avec quelle fréquence utilisez-vous le vélo ?"
question[1] = u"Quels modes de transport avez-vous été amené à utiliser pendant ces 30 derniers jours ?"
question[2] = u"Cherchez-vous à réduire l’usage de votre voiture ?"
question[3] = u"Votre opinion des vélos:"
question[4] = u"Votre opinion des voitures:"
question[5] = u"Cette description traduit mon état d'esprit et/ou ma pratique du vélo"
question[6] = u"Expliquez pourquoi cela correspond ou ne correspond pas à votre état d'esprit ou à votre pratique du vélo"
question[7] = u"L'étape dans laquelle je suis situé correspond à mon état d'esprit et/ou ma pratique du vélo"
question[8] = u"Si vous n'êtes pas d'accord, indiquez l'étape qui semble vous correspondre le mieux"

# Consignes aux questions
consigne[0] = u"(Veuillez selectionner 1 réponse)"
consigne[1] = u"(Veuillez choisir toutes les réponses qui conviennent)"
consigne[2] = u"(Veuillez selectionner 1 réponse)"
consigne[3] = u"(Veuillez selectionner de 1 à 3 réponse(s))"
consigne[4] = u"(Veuillez selectionner de 1 à 3 réponse(s))"

# Reponses aux questions
reponse[0] = [u"Tous les jours ou presque",
              u"Deux ou trois fois par semaine",
              u"Au moins une fois par semaine",
              u"Au moins une fois par mois",
              u"Au moins une fois par an",
              u"Jamais"]
reponse[1] = [u"Voiture particulière",
              u"2 ou 3 roues motorisé",
              u"Transport en commun - réseau urbain",
              u"Transport en commun - réseau périurbain",
              u"Vélo",
              u"Vélo libre-service",
              u"Marche à pied",
              u"Roller, Skate, Trottinette",
              u"Covoiturage",
              u"Autopartage (Citiz...)",
              u"Taxi",
              u"VTC (Uber...)",
              u"Autre"]
reponse[2] = [u"Oui",
              u"Oui, mais je ne peux pas le faire",
              u"Non",
              u"Je n'y ai pas réfléchi"]
reponse[3] = [u"Rapides",
              u"Lents",
              u"Economiques",
              u"Chers",
              u"Ecologiques",
              u"Polluants",
              u"Fiables",
              u"Pas fiables",
              u"Sécurisés",
              u"Dangereux",
              u"Confortables",
              u"Pas confortables",
              u"Rendent autonome",
              u"Contraignants",
              u"Bons pour la santé",
              u"Mauvais pour la santé"]
reponse[4] = [u"Rapides",
              u"Lentes",
              u"Economiques",
              u"Cheres",
              u"Ecologiques",
              u"Polluantes",
              u"Fiables",
              u"Pas fiables",
              u"Sécurisées",
              u"Dangereuses",
              u"Confortables",
              u"Pas confortables",
              u"Rendent autonome",
              u"Contraignantes",
              u"Bonnes pour la santé",
              u"Mauvaises pour la santé"]
reponse[5] = [u"Tout à fait d'accord",
              u"Plutôt d'accord",
              u"Sans opinion",
              u"Plutôt pas d'accord",
              u"Pas du tout d'accord"]
reponse[6] = None
reponse[7] = [u"Tout à fait d'accord",
              u"Plutôt d'accord",
              u"Sans opinion",
              u"Plutôt pas d'accord",
              u"Pas du tout d'accord"]
reponse[8] = None

# Dictionnaire avec les noms complets
phase_nom = {'M' :u"de maintenance",
             'A' :u"d'action",
             'C' :u"de contemplation",
             'PC':u"de précontemplation",
             'P' :u"de préparation"}

# Dictionnaire avec les descriptions des phases
phase_description = {'M' :u"Bienvenue dans la phase de maintenance",
                     'A' :u"Bienvenue dans la phase d'action",
                     'C' :u"Bienvenue dans la phase de contemplation",
                     'PC':u"Bienvenue dans la phase de précontemplation",
                     'P' :u"Bienvenue dans la phase de préparation"}

# Question finale
question_fin = u"Acceptez-vous de transmettre vos réponses pour analyses à des fins scientifiques ?"
reponses_fin = [u"Oui", u"Non"]
