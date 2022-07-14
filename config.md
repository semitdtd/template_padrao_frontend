# Configurações Template
<p>passo a paso para integração do template ao seu projeto</p>

## Configurações settings.py
<hr>

 ## INSTALLED_APPS
 
 ```
'apps.core'
```

 ## TEMPLATES
 
 ```
'DIRS': [
            BASE_DIR / 'templates'
        ],
```
## Configurações urls do seu projeto
<hr>

 ## urls.py
 
 ```
path('', include('apps.core.urls')),
```



