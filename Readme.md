Projet 3 : Aidez MacGyver à s'échapper ! 

Dépot Github : https://github.com/nicoseng/P3-McGyver.git
Programme rédigé sous Python3 et avec le module Pygame (version 1.9.6)
Projet sous Virtual Env et Git 

Ce document a pour objectif de guider l’utilisateur étape par étape afin de lui permettre de lancer le jeu depuis son ordinateur.

I°) Préparer l’environnement virtuel de développement
    1.	Installer un environnement virtuel de développement depuis votre terminal. (python3 –m venv env)
    2.	Activer l’environnement virtuel en tapant source env/bin/activate. Une mention (env) s’affiche à gauche de votre console.

II°) Activer le jeu 
    1.	 Dans le terminal, entrer python3 main.py. Ce dernier correspond au fichier principal du jeu. 
    2.	 Dans le terminal, entrer le nom du fichier contenant la carte sous forme « brut » : map.txt. La carte correspondant s’affiche graphiquement sur votre écran. 

La carte intitulée map.txt est prise en charge dans un « Sélecteur de carte » (Class MapSelector). Chaque ligne contenue dans carte.txt est ajoutée à une liste initialement vide. Cette étape permet de générer la matrice du labyrinthe.

III°) Jouer au jeu 

	L’objectif du jeu est d’amener notre héros Macgyver vers la sortie du labyrinthe située sur la case où se trouve le gardien. Pour ce faire, notre héros doit au préalable récupérer 3 objets (éther, tube et aiguille) disséminés au hasard dans le labyrinthe afin de pouvoir créer une seringue destinée à endormir le gardien et ainsi rejoindre la sortie. L’obtention des trois objets lors de la présentation au gardien permet alors de remporter de la partie. A défaut de ces objets, le héros meurt et le joueur perd la partie.

•	Se déplacer dans le labyrinthe
        o   Appuyer au choix sur les flèches directionnelles. Le héros ne peut se déplacer que sur des cases vides.

•	Récupérer un objet 
        o   Se déplacer sur la case où se trouve l’objet. L’objet ramassé disparaît du labyrinthe et le compteur inventaire indique le nombre d’objet ramassé. 

•	Gagner/Perdre le jeu 
        o    L’obtention des trois objets lors de la présentation au gardien permet de remporter de la partie. A défaut de ces objets, le héros meurt et le joueur perd la partie. Un message de victoire/défaite s’affiche selon les cas. 
•	Quitter le jeu 
	A tout moment, le joueur peut quitter le jeu. Pour ce faire, deux solutions : 
        o	Choix 1 : Appuyer sur la touche q du clavier. On peut aussi 
        o	Choix 2 : Cliquer directement sur la croix pour fermer la fenêtre.
