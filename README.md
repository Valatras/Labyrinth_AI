# Projet IA Labyrinthe
Nous sommes étudiants à l'École centrale des arts et métiers, Arifcan Yildirim [20144] et Melvin Affoum [21203].
Dans le cadre du cours de monsieur @qlurkin, nous avons programmé une intelligence artificielle permettant de jouer au jeu de société Labyrinthe sur python.



## 🛠 Stratégie
L'IA utilise un algorithme de type Greedy Best First Search. Pour chaque move possible, l'IA attribue une valeur qui dépend de la distance entre la nouvelle position du pion et la position du trésor ciblé. Le move sélectionné sera celui avec la valeur(distance) la plus basse qui est calculé sur base du théorème de pythagore et des coordonnées en x et en y. La réponse renvoyé par l'algorithme est composé de la tuile libre correctement orientée, la porte sur laquelle elle sera jouée, et la nouvelle position du pion.

## 📚 Bibliothèque 
* Nous avons employé la bibliothèque "socket" afin de nous connecter au serveur.
* Nous avons employé la bibliothèqye "sys" afin d'éteindre notre programme s'il y a un problème lors de la connexion ou le code.
* Nous avons employé la bibliothèque "time" afin d'utiliser un timer de quelques instants.
* Nous avons employé la bibliothèque "json" afin de manipuler des fichiers json.