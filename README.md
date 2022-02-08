# TP File - Ynov Python B1

:see_no_evil: _**Il s'agit d'un travail autonomne.**_ :speak_no_evil:

:sparkles: Une fois le TP et le rendu terminé commitez et pushez le dans le repo. :sparkles:
  
### Tips   

:raising_hand: Si vous avez des soucis n'hésitez pas à m'appeler. 
 
 ## Exercice 1 : 
 
 - Lire le fichier `squid.log` et afficher ses lignes.

## Exerice 2 : 
 - Créer une fonction qui lit le fichier `squid.log` et qui affiche toutes les lignes sauf celles possédant le mot `Warning`.

## Exercice 3 : 
 - Créer une fonction qui va print les X dernières lignes d'un fichier. 
   - Pensez aux index des listes (0,1,2,3,...,n) et (-1,-2,...,-n)
   - X doit est fournit en argument de la commande 

## Exercice BONUS : Log Web Reader
 
Le but de ce projet est de faire un pas dans la programmation orienté Infra.
Les logs sont pour un administrateur systeme un outils très important dans la compréhension et le debugging d'une situation de crise. 

Ce programme vous a été demandé par un chef d'équipe qui souhaite exporter les logs d'une machine sur un site internet pour qu'ils puissent être affiché en temps réel sur un écran en salle de crise.


 Il faudra donc réaliser un programme : 
- Qui va ouvrir un fichier log prédéfini
- Lire ce fichier et afficher le contenu sur le terminal en temps réel. Vous devez pouvoir rajouter du texte dans le fichier et le script python doit pouvoir l'afficher. Il faut donc garder le fichier ouvert. Pensez à rajouter un `sleep(1)` entre l'affichage de chaque ligne

- Exporter cet affichage sur un site internet développé en Python
  - Pour cela vous utiliserez le module `Flask` -- Tout le code inhérent a flask est présent dans les sources de ce repo.
  - Pour lancer votre application flask il faut : 
    - exporter une variable d'environnement : `export FLASK_APP=/path/to/your/python/app.py`
    - lancer la commande `flask run` 

Pour rajouter des lignes au fichier vous pouvez utiliser la commande : 
```bash 
for i in $(seq 1 1000);do echo $i >> app.log;sleep 0.5;done
```

###  BONUS_BONUS : 
- Permettre de faire faire un `tail -f -n X` sur le fichier. C'est à dire de choisir d'ignorer les X premières lignes
- Packager cette application dans une image docker 
- Vous pouvez utiliser un environnement virtuel comme Poetry pour gérer les librairies et livrer une application entière (Code, librairie, dépendances etc..)
