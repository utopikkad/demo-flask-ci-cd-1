
build:

# Une cible "prepare" qui fasse l'installation des dépendances du projet
prepare:
	pipenv install

# TODO: ajouter une cible "test" qui teste la qualité du projet (et plante sinon)

test:
	pipenv run pylint *.py


