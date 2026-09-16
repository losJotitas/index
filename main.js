window.addEventListener('DOMContentLoaded', () => {
    if (typeof colegios !== 'undefined' && Array.isArray(colegios)) {
        colegios.forEach(colegio => {
            if (colegio.latitud && colegio.longitud) {
                let popupContenido = `
                    <div style="font-family: Arial, sans-serif; max-width: 220px;">
                        <h3 style="margin: 0 0 5px 0; font-size: 14px; color: #1e3a8a;">${colegio.nombre_colegio}</h3>
                        <p style="margin: 0 0 5px 0; font-size: 12px;"><b>Gestión:</b> ${colegio.gestion}</p>
                        <p style="margin: 0 0 5px 0; font-size: 12px;"><b>Niveles:</b> ${colegio.niveles}</p>
                        <p style="margin: 0; font-size: 12px;"><b>Dirección:</b> ${colegio.direccion}</p>
                    </div>
                `;

                L.marker([colegio.latitud, colegio.longitud])
                    .addTo(map)
                    .bindPopup(popupContenido);
            }
        });
        console.log(`Colegios cargados correctamente: ${colegios.length}`);
    } else {
        console.error("No se encontró el array colegios.");
    }
});