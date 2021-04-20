const book_url = $("#bklink").val();
console.log(book_url);
var loadingPage = pdfjsLib.getDocument(book_url);
loadingPage.promise.then((doc) => {
    const numPages = doc._pdfInfo.numPages;
    doc.getPage(1).then((page) => {
        var canvas = document.getElementById("viewer");
        var context = canvas.getContext("2d");
        var viewport = page.getViewport(1);
        canvas.width = viewport.width;
        canvas.height = viewport.height;
        page.render({
            canvasContext: context,
            viewport: viewport
        });
    });
    console.log(numPages);
});
