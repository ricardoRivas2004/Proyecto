const imagenesFondo = [
    'url(https://i.pinimg.com/originals/8c/b2/2d/8cb22d8ead9b13c226cbff599b35331c.jpg)',
    'url(https://i.pinimg.com/originals/cb/75/08/cb75089d4437359724c28eede200cb53.png)',
    'url(https://static.vecteezy.com/system/resources/previews/024/200/211/original/flat-minimalistic-design-panorama-of-a-mountain-landscape-easy-to-change-colors-vector.jpg)'
];

// Función para cambiar la imagen de fondo cada cierto tiempo
function cambiarFondo() {
    // Obtener un número aleatorio entre 0 y el número total de imágenes
    const indice = Math.floor(Math.random() * imagenesFondo.length);
    // Aplicar la imagen de fondo al body
    document.body.style.backgroundImage = imagenesFondo[indice];
}

cambiarFondo();


setInterval(cambiarFondo, 10000); //tiempo en mlsegundos






