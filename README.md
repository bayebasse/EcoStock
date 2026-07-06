# Pourquoi cette erreur ?

Tu essaies d'accéder à l'URL :

```text
http://127.0.0.1:8000/products/
```

Cependant, dans ton projet Django, les routes sont configurées avec le préfixe **`/api/`**. Les routes disponibles sont notamment :

* `admin/`
* `api/`
* `api/token/`
* `api/token/refresh/`

Par conséquent, Django ne trouve pas la route **`/products/`**, ce qui explique l'erreur **404 Page Not Found**.

## La bonne URL

Tu dois utiliser :

```text
http://127.0.0.1:8000/api/products/
```

et non :

```text
http://127.0.0.1:8000/products/
```

## Pourquoi ?

Dans le fichier `ecostock/urls.py`, tu as probablement la ligne suivante :

```python
path("api/", include("stock.urls")),
```

Cela signifie que **toutes les routes définies dans `stock/urls.py` seront automatiquement précédées de `/api/`**.

Par exemple :

 Fonction             URL correcte               
 ------------------- -------------------------- 
 Liste des produits       `/api/products/`           
 Détail d'un produit `/api/products/1/`         
 Liste des entrepôts  `/api/warehouses/`         
 Déplacer un produit  `/api/products/1/move/`    
Audit d'un entrepôt  `/api/warehouses/1/audit/` 

## Si tu souhaites utiliser `/products/`

Il faudrait modifier le fichier `ecostock/urls.py` en remplaçant :

```python
path("api/", include("stock.urls")),
```

par :

```python
path("", include("stock.urls")),
```

Cependant, pour une API REST, il est recommandé de conserver le préfixe **`/api/`**, car c'est une bonne pratique largement utilisée.

## Conclusion

Le projet ne présente pas d'erreur de fonctionnement. L'erreur provient simplement de l'URL utilisée. Il suffit d'accéder à :

```text
http://127.0.0.1:8000/api/products/
```

pour atteindre correctement l'endpoint des produits.
