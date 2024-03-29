document.addEventListener('DOMContentLoaded', function () {
    let table = new DataTable('#TableIO', {
        paging: true,
        order: false,
        searching: true,
        colReorder: true,
        autoWidth: false,
        fixedHeader: true,
        columns: [{ width: '30%'}, { width: '15%'}, { width: '5%'}, null],
    });
});