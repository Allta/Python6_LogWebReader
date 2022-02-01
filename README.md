# TP Guess The Number - Ynov Python B1

:see_no_evil: _**Il s'agit d'un travail autonomne.**_ :speak_no_evil:

:sparkles: Une fois le TP et le rendu terminé commitez et pushez le dans le repo. :sparkles:
  
### Tips   

:raising_hand: Si vous avez des soucis n'hésitez pas à m'appeler. 
 
 ## Exercice 1: Log Web Reader
 
Le but de ce projet est de faire un pas dans la programmation orienté Infra.
Les logs sont pour un administrateur systeme un outils très important dans la compréhension et le debugging d'une situation de crise. 

Ce programme vous a été demandé par un chef d'équipe qui souhaite exporter les logs d'une machine sur un site internet pour qu'ils puissent être affiché en temps réel sur un écran en salle de crise.


 Il faudra donc réaliser un programme : 
- Qui va ouvrir un fichier log prédéfini
- Lire ce fichier et afficher les logs en temps réel
- Exporter cet affichage sur un site internet développé en Python
  - Pour cela vous utiliserez le module `Flask` -- Tout le code inhérent a flask est présent dans les sources de ce repo.
  - Pour lancer votre application flask il faut : 
    - exporter une variable d'environnement : `export FLASK_APP=/path/to/your/python/app.py`
    - lancer la commande `flask run` 



## Exercice BONUS : 

- Packager cette application dans une image docker
