MarginaliaApp.factory('Book', function (Restangular) {
    var Book;
    Book = {
        get: function () {
            return Restangular
                .one('books')
                .getList();
        },
        create: function (data) {
            return Restangular
                .one('books')
                .customPOST(data);
        }
    };
    return Book;
});