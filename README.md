# INFO731 - Sécurité et Cryptographie

---

Mise en place du système de ~censure~<sub>Sécurisation !</sub> des réseaux du **grand**, **puissant** et **immense** gouvernement de <u>**Freedonia**</u>. Dirigé par les équipes du **génialissime _El Chico_**.

> [!CAUTION]
> Ces documents classifiés "top-secret" ne doivent sous aucun cas être partagés aux chameaux lumineux sous peine de

## Structure du réseau

Le réseau de machines Linux Docker/Kathara est organisé de la manière suivante :

### Composants du réseau

1. **Firewall** : Cette machine est la seule à être directement connectée à Internet. Elle contrôle et filtre les requêtes des clients vers Internet.
2. **Machines internes** : 
    - **PC1**
    - **PC2**
    - **PC3**
    - **Premier_Ministre** 
    - **Banque_Centrale**

### Firewall et proxy

Le **firewall** est la passerelle principale entre le réseau interne et Internet. Il bloque certains noms de domaine et implémente un proxy pour filtrer les requêtes illégales provenant des machines du commun des mortels, seulement autorisées à accéder à Internet via ce proxy. Les ordinateurs du **Premier Ministre** et de la **Banque Centrale** ont un laissez-passer pour accéder directement à Internet en passant par le proxy mais sans vérification des règles de filtrage.

### Schéma du Réseau

```
    Internet
        |
    +---+----+
    |Firewall|
    |+ Proxy |
    +---+----+
        |
        |
+---+---+---+---+---+---+---+---+---+
|       |       |       |           |
PC1     PC2     PC3     Ministre*   Banque_Centrale*
                        (*:Bypass Proxy)
```

Le **Firewall** est le nœud central de la sécurité du réseau. Il assure que toutes les communications passent par son filtre de proxy, excepté pour les machines sans restriction, comme **Premier_Ministre** et **Banque_Centrale**.

## Fonctionnement du Firewall

Le **Firewall** est une machine faisant office de passerelle entre le réseau interne et Internet. Il est configuré pour mettre en place des routes pour les différentes machines du réseau. En premier lieu, il autorise l'utilisation de toutes les routes pour les machines privilégiées, puis il bloque les routes vers les domaines interdits pour les autres machines.

Les adresses IP privilégiées doivent être ajoutées au fichier `/scripts/allowerd_ips.txt` et les domaines interdits doivent être ajoutés au fichier `/scripts/blocked_sites.txt`.

## Fonctionnement du proxy

Le proxy est un serveur qui agit comme un intermédiaire entre les clients et les serveurs. Chaque requête HTTP est interceptée par le proxy, qui envoie ensuite lui-même la requête au serveur, puis renvoie la réponse au client si elle est autorisée. Toute requête contenant des mots-clés sensibles sera bloquée et son auteur se verra convoqué par les autorités compétentes _afin d'échanger sur ses perspectives d'avenir_... :wink: 

Les mots-clés sensibles doivent être ajoutés au fichier `/scripts/swear_words.csv`, une requête est immédiatement interceptée si elle contient un mot-clé de cette liste.

> [!TIP]
> Le proxy peut aussi être utilisé pour cacher l'adresse IP des clients !

## Prérequis

- [Docker](https://docs.docker.com/get-docker/)

- [Kathara](https://www.kathara.org/)

- Installation de l'image Docker `kathara/base` :

```bash
docker pull kathara/base
```

- Création de l'image Docker `kathara-freedonia` spécifique à ce projet (à partir du Dockerfile) :

```bash
docker build -t kathara-freedonia . # à exécuter dans le répertoire du projet
```

## Lancement du réseau

- Lancer docker

- Lancer le lab Kathara :

```bash
kathara lstart # à exécuter dans le répertoire du projet
```

- Activer le proxy sur le firewall :

```bash
./scripts/start_proxy.sh
```

- Faire une requête HTTP depuis une machine du réseau :

```bash
curl httpbin.org # Par exemple
```

Si la requête est autorisée, la réponse sera affichée. Sinon, un message d'erreur 403 (Forbidden) sera retourné.

## Arrêt du réseau

- Arrêter le lab Kathara :

```bash
kathara lclean # à exécuter dans le répertoire du projet
```

---

© 2024 - INFO731 - Tous droits réservés - Propriété du gouvernement de Freedonia.
Pour plus d'informations, veuillez consulter les [conditions générales d'utilisation](#).