MarginaliaApp.controller('HomeDetailCtrl', function($scope, Book) {
    Book.get().then(function(books) {
        $scope.books = books;
    });
})