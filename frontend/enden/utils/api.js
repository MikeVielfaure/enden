async function fetchWithAuth(url, options = {}) {
    let accessToken = localStorage.getItem("access_token");

    // 1️⃣ Vérifie si le token est expiré AVANT l’appel API
    if (isTokenExpired(accessToken)) {
        accessToken = await refreshAccessToken();
        if (!accessToken) {
            window.location.href = "/login/
            
            ";  // Redirection si plus de token
            return;
        }
        localStorage.setItem("access_token", accessToken);
    }

    // 2️⃣ Ajoute le token dans la requête API finale
    options.headers = {
        ...options.headers,
        "Authorization": `Bearer ${accessToken}`
    };

    return fetch(url, options).then(res => res.json());
}

// Vérifie si le token est expiré (basé sur l'exp claim du JWT)
function isTokenExpired(token) {
    if (!token) return true;
    const payload = JSON.parse(atob(token.split(".")[1]));
    return payload.exp * 1000 < Date.now();
}

// Rafraîchit le token si expiré
async function refreshAccessToken() {
    const response = await fetch("https://api.example.com/refresh_token/", {
        method: "POST",
        credentials: "include",  // Utilise le refresh_token stocké en cookie
    });

    if (!response.ok) return null;
    const data = await response.json();
    return data.access_token;
}
