#!/usr/bin/env python3

import numpy as np

version = '1.0'

def logic_tree(choix_final, reponses):

    # Reponses aux questions Oui/Non de l'arbre
    phase = None

    # === REGARDER CE QU'IL A REPONDU === #
    i0 = reponses[0].index(choix_final[0][0])

    # === REGARDER SI LE MOT VELO APPARAIT DANS UNE DE SES REPONSES === #
    i1 = np.any([True if u"Vélo" in c else False for c in choix_final[1]])

    # === REGARDER SI IL A REPONDE OUI (QUESTION: QUE FAIRE DE OUI, MAIS...) === # 
    i2 = reponses[2].index(choix_final[2][0])

    # === METTRE +1 AUX REPONSES POSITIVES ET -1 AUX REPONSES NEGATIVES (QUESTION: QUE FAIRE SI L'OPINION EST NEUTRE) === #
    i3 = np.sum([+1 if reponses[3].index(c) % 2 == 0 else -1 for c in choix_final[3]])

    # === METTRE +1 AUX REPONSES POSITIVES ET -1 AUX REPONSES NEGATIVES (QUESTION: QUE FAIRE SI L'OPINION EST NEUTRE) === #
    i4 = np.sum([+1 if reponses[4].index(c) % 2 == 0 else -1 for c in choix_final[4]])

    # ========================= #
    #                           #
    # CONSTRUCTION DU SCHEMA #3 #
    #                           #
    # ========================= #
    if (i0 == 0) or (i0 == 1):
        # OUI (Utilise les 30 derniers jours)
        if (i1):
            phase = 'M'
        # NON (Utilise les 30 derniers jours)
        else:
            # OUI (Reduc. Voiture)
            if (i2 == 0):
                phase = 'P'
            # NON (Reduc. Voiture)
            else:
                # AVIS POSITIF DU VELO ET NEGATIF DE LA VOITURE
                if (i3 > 0) and (i4 < 0):
                    phase = 'C'
                # AVIS NON TRANCHE
                else:
                    phase = 'PC'

    # ========================= #
    #                           #
    # CONSTRUCTION DU SCHEMA #2 #
    #                           #
    # ========================= #
    elif i0 == 2 or i0 == 3:
        # OUI (Utilise les 30 derniers jours)
        if (i1):
            # OUI (Reduc. Voiture)
            if (i2 == 0):
                # Au moins une fois par semaine
                if (i0 == 2):
                    phase = 'A'
                # Au moins une fois par mois
                else:
                    phase = 'P'
            # NON (Reduc. Voiture)
            else:
                # AVIS POSITIF DU VELO ET NEGATIF DE LA VOITURE
                if (i3 > 0) and (i4 < 0):
                    # Au moins une fois par semaine
                    if (i0 == 2):
                        phase = 'P'
                    # Au moins une fois par mois
                    else:
                        phase = 'C'
                # AVIS NON TRANCHE
                else:
                    # Au moins une fois par semaine
                    if (i0 == 2):
                        phase = 'C'
                    # Au moins une fois par mois
                    else:
                        phase = 'PC'
        # NON (Utilise les 30 derniers jours)
        else:
            # OUI (Reduc. Voiture)
            if (i2 == 0):
                # AVIS POSITIF DU VELO ET NEGATIF DE LA VOITURE
                if (i3 > 0) and (i4 < 0):
                    # Au moins une fois par semaine
                    if (i0 == 2):
                        phase = 'P'
                    # Au moins une fois par mois
                    else:
                        phase = 'C'
                # AVIS NON TRANCHE
                else:
                    # Au moins une fois par semaine
                    if (i0 == 2):
                        phase = 'C'
                    # Au moins une fois par mois
                    else:
                        phase = 'PC'
            # NON (Reduc. Voiture)
            else:
                # Au moins une fois par semaine
                if (i0 == 2):
                    phase = 'C'
                # Au moins une fois par mois
                else:
                    phase = 'PC'

    # ========================= #
    #                           #
    # CONSTRUCTION DU SCHEMA #1 #
    #                           #
    # ========================= #
    elif i0 == 4 or i0 == 5:
        # OUI (Utilise les 30 derniers jours)
        if (i1):
            # OUI (Reduc. Voiture)
            if (i2 == 0):
                # AVIS POSITIF DU VELO ET NEGATIF DE LA VOITURE
                if (i3 > 0) and (i4 < 0):
                    phase = 'C'
                # AVIS NON TRANCHE
                else:
                    phase = 'PC'
            # NON (Reduc. Voiture)
            else:
                # AVIS POSITIF DU VELO ET NEGATIF DE LA VOITURE
                if (i3 > 0) and (i4 < 0):
                    phase = 'C'
                # AVIS NON TRANCHE
                else:
                    phase = 'PC'
        # NON (Utilise les 30 derniers jours)
        else:
            # OUI (Reduc. Voiture)
            if (i2 == 0):
                # AVIS POSITIF DU VELO ET NEGATIF DE LA VOITURE
                if (i3 > 0) and (i4 < 0):
                    phase = 'C'
                # AVIS NON TRANCHE
                else:
                    phase = 'PC'
            # NON (Reduc. Voiture)
            else:
                phase = 'PC'

    # All done
    return phase
