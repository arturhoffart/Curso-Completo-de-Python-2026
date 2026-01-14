// SCRIPT PARA CRIAÇÃO DE TEMPLATE DE APOSTILA PYTHON NO ADOBE INDESIGN
// Versão corrigida – compatível com InDesign 20+
// Desenvolvido por Manus AI

app.scriptPreferences.measurementUnit = MeasurementUnits.MILLIMETERS;

// ============================
// 1. CRIAÇÃO DO DOCUMENTO
// ============================

var doc = app.documents.add();

doc.documentPreferences.pageWidth  = 210; // A4
doc.documentPreferences.pageHeight = 297; // A4
doc.documentPreferences.facingPages = false; // ❗ CORREÇÃO AQUI
doc.documentPreferences.pagesPerDocument = 1;

// Garante que a primeira página é direita
doc.pages[0].side = PageSideOptions.RIGHT_HAND;

// ============================
// 2. MARGENS
// ============================

var page = doc.pages[0];

page.marginPreferences.top    = 20;
page.marginPreferences.bottom = 20;
page.marginPreferences.left   = 25;
page.marginPreferences.right  = 20;

// ============================
// 3. FRAME DE TEXTO PRINCIPAL
// ============================

page.textFrames.add({
    geometricBounds: [
        page.marginPreferences.top,
        page.marginPreferences.left,
        doc.documentPreferences.pageHeight - page.marginPreferences.bottom,
        doc.documentPreferences.pageWidth - page.marginPreferences.right
    ],
    textFramePreferences: {
        textColumnCount: 1
    }
});

// ============================
// 4. CORES
// ============================

function addColor(name, rgb) {
    var c;
    try {
        c = doc.colors.itemByName(name);
        c.name;
    } catch (e) {
        c = doc.colors.add({
            name: name,
            model: ColorModel.PROCESS,
            space: ColorSpace.RGB,
            colorValue: rgb
        });
    }
    return c;
}

var corTexto      = addColor("Texto Principal", [51, 51, 51]);
var corTitulo     = addColor("Titulos", [0, 86, 179]);
var corCodigo     = addColor("Codigo", [0, 0, 0]);
var corFundoCode  = addColor("Fundo Codigo", [248, 248, 248]);
var corLegenda    = addColor("Legenda Imagem", [102, 102, 102]);

// ============================
// 5. ESTILOS DE PARÁGRAFO
// ============================

var base = doc.paragraphStyles.add({
    name: "Base",
    fontFamily: "Open Sans",
    fontStyle: "Regular",
    pointSize: 10,
    leading: 14,
    fillColor: corTexto,
    justification: Justification.LEFT_ALIGN,
    hyphenation: false
});

doc.paragraphStyles.add({
    name: "Corpo do Texto",
    basedOn: base,
    spaceBefore: 3,
    spaceAfter: 3
});

doc.paragraphStyles.add({
    name: "H1 - Titulo Principal",
    basedOn: base,
    fontStyle: "Bold",
    pointSize: 24,
    leading: 28,
    fillColor: corTitulo,
    spaceBefore: 15,
    spaceAfter: 10
});

doc.paragraphStyles.add({
    name: "H2 - Secao",
    basedOn: base,
    fontStyle: "Bold",
    pointSize: 18,
    leading: 22,
    fillColor: corTitulo,
    spaceBefore: 12,
    spaceAfter: 8
});

doc.paragraphStyles.add({
    name: "Bloco de Codigo",
    fontFamily: "Fira Code",
    fontStyle: "Regular",
    pointSize: 9,
    leading: 12,
    fillColor: corCodigo,
    paragraphShadingColor: corFundoCode,
    paragraphShadingTopOffset: 3,
    paragraphShadingBottomOffset: 3,
    paragraphShadingLeftOffset: 3,
    paragraphShadingRightOffset: 3,
    spaceBefore: 6,
    spaceAfter: 6,
    hyphenation: false
});

doc.paragraphStyles.add({
    name: "Legenda de Imagem",
    basedOn: base,
    pointSize: 8,
    leading: 10,
    fillColor: corLegenda,
    justification: Justification.CENTER_ALIGN
});

// ============================
// 6. ESTILO DE CARACTERE (INLINE CODE)
// ============================

doc.characterStyles.add({
    name: "Codigo Inline",
    fontFamily: "Fira Code",
    fontStyle: "Regular",
    pointSize: 9,
    fillColor: corCodigo
});

// ============================
// FINAL
// ============================

alert("✅ Template de Apostila Python criado com sucesso!\nSem erros de compatibilidade.");
