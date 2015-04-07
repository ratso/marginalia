MarginaliaApp.controller('BooksCtrl', function ($scope, Book) {
    Book.get().then(function (books) {
        $scope.books = books;
    });
});