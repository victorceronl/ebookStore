const axios = require("axios");
const cheerio = require("cheerio");

const URL = "https://example.com/ebooks"; // 🔗 Cambia esto por la URL real de la tienda

async function scrapearEbooks() {
  try {
    // Descargar la página
    const { data } = await axios.get(URL);

    // Cargar en cheerio (como un mini-jQuery)
    const $ = cheerio.load(data);

    // Array para guardar ebooks
    const ebooks = [];

    // Ajusta los selectores según la estructura de la tienda
    $(".ebook-item").each((i, el) => {
      const titulo = $(el).find(".ebook-title").text().trim();
      const precio = $(el).find(".ebook-price").text().trim();
      const enlace = $(el).find("a").attr("href");

      ebooks.push({ titulo, precio, enlace });
    });

    console.log("📚 Ebooks encontrados:");
    console.table(ebooks);
  } catch (error) {
    console.error("❌ Error en el scraping:", error.message);
  }
}

scrapearEbooks();
