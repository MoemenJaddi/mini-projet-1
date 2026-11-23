# Mini-projet 1 : Application Flask conteneurisée

## Description
Petite application web Flask qui affiche un message d'accueil configurable.
Elle expose aussi `/version` (depuis la version 1.0.1).

## Image Docker Hub
`TON_USERNAME/mini-projet-1`

| Tag     | Description                              |
|---------|------------------------------------------|
| `1.0.0` | Première version                         |
| `1.0.1` | Ajout de la route `/version`             |
| `1.0`   | Alias : pointe toujours vers le dernier 1.0.x |

## Lancer l'application (sans construire)
```bash
docker run -d --name app -p 8080:5000 \
  -e APP_MESSAGE="Bonjour !" \
  --memory 256m --cpus 0.5 \
  TON_USERNAME/mini-projet-1:1.0
```
Puis : `curl http://localhost:8080` et `curl http://localhost:8080/version`

## Variables d'environnement
| Variable      | Défaut                    | Rôle                    |
|---------------|---------------------------|-------------------------|
| `APP_MESSAGE` | `Bonjour depuis Docker !` | Message affiché sur `/` |

## Port
L'application écoute sur le port **5000** dans le conteneur
(publié ici sur 8080 avec `-p 8080:5000`).

## Consulter l'état
```bash
docker ps
docker logs app
docker inspect app
```

## Arrêter et nettoyer
```bash
docker rm -f app
```

## Construire soi-même (optionnel)
```bash
git clone <url-du-depot>
cd mini-projet-1
docker build -t mini-projet-1:1.0.1 .
```
